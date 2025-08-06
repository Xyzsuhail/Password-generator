
# 🔐 Password Generator

A customizable random password generator built using Python.  
This tool allows users to create secure passwords by choosing the desired length and character types (letters, numbers, special characters).

---

## 🚀 Features

- Generate strong, random passwords
- User-defined password length
- Option to include:
  - ✅ Letters (uppercase & lowercase)
  - ✅ Numbers
  - ✅ Special characters
- Basic input validation to ensure secure password generation

---

## 📸 Demo

- Enter the length of the password you want: 12
- Do you want letters? yes
- Do you want numbers? yes
- Do you want to add special characters? yes
- Your new password is: aG7!kd9@Qw&z

---

## 🧠 How It Works

    1. The script takes the desired password length from the user.
    2. It asks whether to include:
        - Letters (`string.ascii_letters`)
        - Numbers (`string.digits`)
        - Special characters (`string.punctuation`)
    3. Based on user choices, a character set is built.
    4. Random characters are picked from this set to form a     password.

---

## ⚙️ Requirements

- Python 3.x  
- No external libraries needed (uses Python's built-in `random` and `string` modules)

---

## 📝 Usage

# Clone the repository
git clone https://github.com/your-username/password-generator.git

# Navigate into the project directory
cd password-generator

# Run the script
python password_generator.py
---

## 📂 File Structure
- bash
-  Copy
- Edit
- password-generator/
- │
- ├── password_generator.py   # Main script
- └── README.md               # Project documentation
---

## 🛡️ License
This project is open-source and available under the MIT License.
---

## 🙌 Author
Made with 💻 by Mohamed Souhail
---




