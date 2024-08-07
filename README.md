# OrgAssist: AI-Powered Organizational Chatbot

OrgAssist is an AI chatbot designed to provide information, answer FAQs, and handle complaints for organizations. This project aims to streamline communication and support for users interacting with your organization.

## Features

- AI-powered chatbot for answering organization-related queries
- FAQ module for quick access to common information
- Complaint reporting system integrated within the chat interface

## Getting Started

To use OrgAssist on your local system, follow these steps:

### Prerequisites

- Python 3.7 or higher
- Git

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/blackwolf2902/Internal-Hackathon.git
   ```

2. Navigate to the project directory:
   ```
   cd Internal-Hackathon
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Start the chatbot application:
   ```
   python main.py
   ```

2. Open your web browser and go to `http://localhost:5000` (or the appropriate address if different).

3. Interact with the chatbot through the web interface.

## Configuration

To customize the chatbot for your organization:

1. Update the FAQ database in `data/faqs.json` with your organization's information.
2. Modify the complaint handling logic in `modules/complaint_handler.py` to fit your organization's processes.
3. Adjust the AI model parameters in `config/ai_config.yml` if necessary.

## Contributing

We welcome contributions to OrgAssist! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Support

For support or questions, please open an issue in the GitHub repository or contact our team at support@orgassist.com.
