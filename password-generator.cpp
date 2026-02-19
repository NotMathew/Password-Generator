#include <algorithm>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <random>
#include <sstream>
#include <string>
#include <vector>

#ifdef _WIN32
#include <windows.h>
#endif

//  Clipboard
bool copyToClipboard(const std::string &text) {
#ifdef _WIN32
  if (!OpenClipboard(nullptr))
    return false;
  EmptyClipboard();
  HGLOBAL hMem = GlobalAlloc(GMEM_MOVEABLE, text.size() + 1);
  if (!hMem) {
    CloseClipboard();
    return false;
  }
  memcpy(GlobalLock(hMem), text.c_str(), text.size() + 1);
  GlobalUnlock(hMem);
  SetClipboardData(CF_TEXT, hMem);
  CloseClipboard();
  return true;
#else
  FILE *pipe = nullptr;
#if defined(__APPLE__)
  pipe = popen("pbcopy", "w");
#else
  pipe = popen("xclip -selection clipboard 2>/dev/null || xsel --clipboard "
               "--input 2>/dev/null",
               "w");
#endif
  if (!pipe)
    return false;
  fwrite(text.c_str(), 1, text.size(), pipe);
  pclose(pipe);
  return true;
#endif
}

//  Password generation
std::string generatePassword(int length, const std::string &charset) {
  std::random_device rd;
  std::mt19937 rng(rd());
  std::uniform_int_distribution<size_t> dist(0, charset.size() - 1);
  std::string password;
  password.reserve(length);
  for (int i = 0; i < length; ++i)
    password += charset[dist(rng)];
  return password;
}

//  Input helpers
int getPositiveIntInput(const std::string &prompt) {
  int value;
  while (true) {
    std::cout << prompt;
    if (std::cin >> value && value > 0) {
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
      return value;
    }
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "Error: Please enter a valid positive number.\n";
  }
}

//  Character set selection
//  Returns chosen charset string.
//  safeMode is set to true if user chose option 6.

std::string getCharacterSet(bool &safeMode) {
  // Full special chars (may break vulnerable programs)
  const std::string specialFull = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
  // Safe special chars: no quotes, spaces, backtick, backslash, angle brackets
  const std::string specialSafe = "!#$%&()*+,-./:;=?@[]^_{}~";

  const std::string lowercase = "abcdefghijklmnopqrstuvwxyz";
  const std::string uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const std::string digits = "0123456789";

  while (true) {
    std::cout << "\nChoose character sets to include in the password:\n";
    std::cout << "  1. Lowercase letters (a-z)\n";
    std::cout << "  2. Uppercase letters (A-Z)\n";
    std::cout << "  3. Digits (0-9)\n";
    std::cout << "  4. Special characters  (all: "
                 "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)\n";
    std::cout << "  5. All character sets\n";
    std::cout << "  6. Program-safe special characters\n";
    std::cout << "     (excludes: ' \" ` \\ < > and spaces - safe for CLI,\n";
    std::cout << "     config files, SQL, HTML, environment variables, etc.)\n";
    std::cout << "Enter the numbers of your choices (e.g. 123, 5, or 6): ";

    std::string choices;
    std::getline(std::cin, choices);

    if (choices.empty()) {
      std::cout << "Error: You must enter at least one choice.\n";
      continue;
    }

    bool valid = std::all_of(choices.begin(), choices.end(),
                             [](char c) { return c >= '1' && c <= '6'; });
    if (!valid) {
      std::cout << "Error: Invalid input. Please use only digits 1-6.\n";
      continue;
    }

    // Option 6 overrides everything — build safe set
    if (choices.find('6') != std::string::npos) {
      safeMode = true;
      std::cout << "  [Safe mode enabled: problematic characters excluded]\n";
      return lowercase + uppercase + digits + specialSafe;
    }

    safeMode = false;
    std::string charset;

    if (choices.find('5') != std::string::npos) {
      charset = lowercase + uppercase + digits + specialFull;
    } else {
      if (choices.find('1') != std::string::npos)
        charset += lowercase;
      if (choices.find('2') != std::string::npos)
        charset += uppercase;
      if (choices.find('3') != std::string::npos)
        charset += digits;
      if (choices.find('4') != std::string::npos)
        charset += specialFull;
    }

    if (charset.empty()) {
      std::cout << "Error: You must select at least one character set.\n";
      continue;
    }
    return charset;
  }
}

//  File export
bool exportToFile(const std::vector<std::string> &passwords) {
  auto now = std::chrono::system_clock::now();
  std::time_t t = std::chrono::system_clock::to_time_t(now);
  std::tm tm_buf{};
#ifdef _WIN32
  localtime_s(&tm_buf, &t);
#else
  localtime_r(&t, &tm_buf);
#endif
  std::ostringstream oss;
  oss << "generated_passwords_" << std::put_time(&tm_buf, "%Y%m%d_%H%M%S")
      << ".txt";
  std::string filename = oss.str();

  std::ofstream file(filename);
  if (!file.is_open()) {
    std::cout << "Error: Unable to write to file. Check your permissions.\n";
    return false;
  }
  for (size_t i = 0; i < passwords.size(); ++i)
    file << (i + 1) << ". " << passwords[i] << "\n";

  std::cout << "Passwords exported to: " << filename << "\n";
  return true;
}

//  Main
int main() {
  std::cout << R"(
      .--.
    /.-. '----------.
    \'-' .--"--""-"-'
     '--'
    Password-Generator (C++)
)" << "\n";

  int length = getPositiveIntInput("Enter the desired password length: ");
  int count =
      getPositiveIntInput("Enter the number of passwords to generate: ");
  bool safeMode = false;
  std::string charset = getCharacterSet(safeMode);

  while (true) {
    // Generate
    std::vector<std::string> passwords;
    passwords.reserve(count);

    std::cout << "\nGenerated Passwords:\n";
    for (int i = 0; i < count; ++i) {
      std::string pw = generatePassword(length, charset);
      passwords.push_back(pw);
      std::cout << (i + 1) << ". " << pw << "\n";
    }

    // Settings summary
    std::cout << "\n[Current settings]"
              << "  Length: " << length << "  |  Count: " << count;

    // Action menu
    while (true) {
      std::cout << "\nWhat would you like to do?\n";
      std::cout << "  1. Copy to clipboard\n";
      std::cout << "  2. Export to text file\n";
      std::cout << "  3. Both copy and export\n";
      std::cout << "  4. Regenerate passwords\n";
      std::cout << "  5. Change settings (length / count / character set)\n";
      std::cout << "  6. Exit without saving\n";
      std::cout << "Enter your choice (1-6): ";

      std::string choice;
      std::getline(std::cin, choice);

      if (choice == "1") {
        std::string all;
        for (auto &p : passwords)
          all += p + "\n";
        if (copyToClipboard(all))
          std::cout << "All passwords copied to clipboard.\n";
        else
          std::cout << "Clipboard unavailable on this system.\n";
        return 0;

      } else if (choice == "2") {
        exportToFile(passwords);
        return 0;

      } else if (choice == "3") {
        std::string all;
        for (auto &p : passwords)
          all += p + "\n";
        if (copyToClipboard(all))
          std::cout << "Passwords copied to clipboard.\n";
        else
          std::cout << "Clipboard unavailable on this system.\n";
        exportToFile(passwords);
        return 0;

      } else if (choice == "4") {
        std::cout << "Regenerating...\n";
        break; // re-enter outer loop → regenerate with same settings

      } else if (choice == "5") {
        // ── Change settings submenu ──────────────────────
        std::cout << "\n--- Change Settings ---\n";
        std::cout << "What do you want to change?\n";
        std::cout << "  1. Password length  (current: " << length << ")\n";
        std::cout << "  2. Number of passwords to generate  (current: " << count
                  << ")\n";
        std::cout << "  3. Character set\n";
        std::cout << "  4. Change all\n";
        std::cout << "  5. Cancel\n";
        std::cout << "Enter your choice (1-5): ";

        std::string sub;
        std::getline(std::cin, sub);

        bool changed = false;

        if (sub == "1" || sub == "4") {
          length = getPositiveIntInput("Enter new password length: ");
          changed = true;
        }
        if (sub == "2" || sub == "4") {
          count = getPositiveIntInput("Enter new number of passwords: ");
          changed = true;
        }
        if (sub == "3" || sub == "4") {
          charset = getCharacterSet(safeMode);
          changed = true;
        }
        if (sub == "5") {
          std::cout << "No changes made.\n";
        } else if (!changed) {
          std::cout << "Invalid choice. No changes made.\n";
        } else {
          std::cout << "Settings updated. Regenerating passwords...\n";
        }
        break; // re-enter outer loop → regenerate with new settings

      } else if (choice == "6") {
        std::cout << "Exiting without saving.\n";
        return 0;

      } else {
        std::cout << "Invalid choice. Enter a number between 1 and 6.\n";
      }
    }
  }
}