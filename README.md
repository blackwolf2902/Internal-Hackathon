# OrgAssist: AI-Powered Organizational Chatbot

OrgAssist is an AI chatbot designed to provide information, answer FAQs, and handle complaints for organizations. This project aims to streamline communication and support for users interacting with your organization.

## Features

- AI-powered chatbot for answering organization-related queries
- FAQ module for quick access to common information
- Complaint reporting system integrated within the chat interface
- MongoDB database for data storage

## Project Structure

```
Org-Assist/
├── static/
├── templates/
├── app.py
├── chat.py
├── data.pth
├── db.py
├── intents.json
├── model.py
├── nltk_utils.py
├── output_data.json
├── sample.py
├── train.py
├── LICENSE
└── README.md
```

## Getting Started

To use OrgAssist on your local system, follow these steps:

### Prerequisites

- Python 3.7 or higher
- Git
- MongoDB

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/blackwolf2902/Org-Assist.git
   ```

2. Navigate to the project directory:
   ```
   cd Internal-Hackathon
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Configuration

1. MongoDB Setup:
   - Install MongoDB on your system if you haven't already.
   - Start the MongoDB service.
   - Update the MongoDB connection string in `db.py` if necessary.

2. Chatbot Training:
   - Review and modify the `intents.json` file to customize the chatbot's knowledge base.
   - Run the training script:
     ```
     python train.py
     ```

3. Application Configuration:
   - Check `app.py` and update any configuration variables if needed.

### Usage

1. Start the chatbot application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://localhost:5000` (or the appropriate address if different).

3. Interact with the chatbot through the web interface.

## Development

- `model.py`: Contains the neural network model for the chatbot.
- `nltk_utils.py`: Provides natural language processing utilities.
- `chat.py`: Implements the chatbot's conversation logic.
- `db.py`: Handles database operations with MongoDB.
- `sample.py`: Includes sample code or tests (refer to file contents for specific usage).

## Training the Model

To retrain the model with updated intents:

1. Modify the `intents.json` file with new patterns and responses.
2. Run the training script:
   ```
   python train.py
   ```
3. The new model will be saved as `data.pth`.

## Contributing

We welcome contributions to OrgAssist! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support or questions, please open an issue in the GitHub repository.
