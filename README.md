# BabyAI

#### Video Demo: <URL HERE>

#### Description:
This project implements a conversational AI chatbot utilizing deep learning techniques, powered by PyTorch. The chatbot is designed to understand user input, classify it into predefined categories (intents), and provide contextually relevant responses. It features both text-based and voice-based interaction, allowing users to communicate through spoken language or typed commands.

The system uses Natural Language Processing (NLP) techniques such as tokenization, stemming, and bag-of-words representations to process and interpret user input. The neural network model classifies input into different intents, and based on the predicted intent, the chatbot selects and delivers an appropriate response. 

Key features include:
- **Speech Recognition**: Converts user voice input into text using the `speech_recognition` library.
- **Text-to-Speech**: Converts the chatbot's text response into speech using `pyttsx3`, providing an interactive experience.
- **Neural Network Classifier**: A custom-built feed-forward neural network model classifies user input into predefined intents.
- **Dynamic Response Generation**: The chatbot selects responses from a variety of predefined options for each intent.

---

## Table of Contents:
- [Project Files Breakdown](#project-files-breakdown)
- [Key Design Choices](#key-design-choices)
- [Training and Model Evaluation](#training-and-model-evaluation)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Project Files Breakdown

### `main.py`
This is the entry point of the chatbot. It manages the user interaction, including:
1. **Listening to the User**: Captures voice input using the `Listen()` function from the `listen.py` module.
2. **Preprocessing Input**: Tokenizes and vectorizes the input using a bag-of-words model.
3. **Intent Classification**: The input is passed through the neural network model to predict the intent.
4. **Response Generation**: Based on the predicted intent, a response is chosen from a predefined set and communicated back to the user via text-to-speech using the `Say()` function from the `speak.py` module.

### `Brain.py`
Contains the definition of the neural network used for intent classification. The network has three fully connected layers, with ReLU activations between the layers. It processes bag-of-words vectors and outputs a predicted intent label.

### `Listen.py`
This file handles capturing and recognizing user input via voice. It uses the `speech_recognition` library to transcribe spoken words into text.

### `Speak.py`
The `Speak.py` module provides the functionality to convert text into speech. Using the `pyttsx3` library, it enables the chatbot to respond to the user audibly, enhancing user interaction.

### `NeuralNetwork.py`
Contains utility functions for preprocessing text:
- **`tokenize()`**: Splits input sentences into individual words.
- **`stem()`**: Applies stemming to reduce words to their root form.
- **`bag_of_words()`**: Converts tokenized sentences into a binary vector representation (bag-of-words model), indicating the presence or absence of words in the input sentence.

### `Train.py`
The training script for the neural network. It processes the input data (intents and patterns), builds the training dataset, and trains the model using backpropagation. The trained model is then saved as `TrainData.pth` for future use.

### `intents.json`
Contains the dataset for training the chatbot. It includes predefined intents with corresponding patterns (user input examples) and responses. The chatbot learns to map patterns to the appropriate intent and select a corresponding response.

Example of intent structure:
```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hello", "Hi", "Hey"],
      "responses": ["Hello!", "Hi there!", "Greetings!"]
    }
  ]
}

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DiwakarTheDev/BabyAI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd BabyAI
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the training script:
   ```bash
   python AI/Train.py
   ```

## Design Decisions

### Choice of Framework
We chose Python and PyTorch as the primary frameworks for this project due to their widespread adoption, strong community support, and robust libraries for machine learning and reinforcement learning.

### Modular Architecture
The project follows a modular design philosophy to promote reusability and ease of debugging. Each module has a single responsibility, making it straightforward to extend or replace components.

### Customizable Models and Environments
By decoupling model architectures and environment definitions, BabyAI allows developers to experiment with different designs without modifying the core framework.

## Future Work

- **Advanced RL Algorithms**: Integrate more state-of-the-art RL algorithms, such as SAC and TD3.
- **Pretrained Models**: Provide pretrained models for common tasks to reduce training time.
- **Enhanced NLP Support**: Expand the natural language processing capabilities for more complex interactions.
- **Visualization Tools**: Implement tools for visualizing training progress and agent behavior.

## Contributions
Contributions to BabyAI are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
