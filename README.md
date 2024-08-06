# Brigade Browser

Brigade Browser is a custom web browser built using PyQt5 and Qt WebEngine. It features tabbed browsing, a customizable toolbar, and a smart search bar with autocomplete functionality based on your search history.

## Features

- **Tabbed Browsing:** Open multiple tabs with an interface for managing and closing them.
- **Customizable Toolbar:** Includes back, forward, reload, home, and new tab buttons.
- **Smart Search Bar:** Autocomplete suggestions based on search history.
- **Stylized Tabs:** Enhanced tab appearance with hover effects and custom styles.
- **Homepage:** Set a custom homepage that opens on startup or when creating new tabs.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/brigade-browser.git
    cd brigade-browser
    ```

2. **Create a Virtual Environment (Optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application:**

    ```bash
    python main.py
    ```

2. **Navigate:**
    - Use the back and forward buttons to navigate through your browsing history.
    - Use the reload button to refresh the current page.
    - Use the home button to navigate to the homepage.
    - Use the new tab button to open a new tab with a custom homepage.

3. **Search Bar:**
    - Type a URL or search term into the search bar and press Enter to navigate.
    - The autocomplete feature suggests URLs based on your search history.

## Customization

- **Icons:** Place your icons in the `icons` directory. Ensure that the paths in the code match the icons you have.
- **Homepage:** Modify the `homepage.html` file in the project directory to set your desired homepage.

## Contributing

Feel free to open issues or submit pull requests to contribute to the development of Brigade Browser. For significant changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
