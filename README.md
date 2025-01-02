# BabyAI

#### Video Demo: <URL HERE>

#### Description:

BabyAI is a foundational artificial intelligence framework aimed at simplifying the development of AI agents for a variety of tasks. This project demonstrates an easy-to-use, modular architecture that combines key principles from reinforcement learning, natural language processing, and robotics, enabling developers to create agents that can interact with and learn from their environments in an intuitive manner.

## Key Features

- **Modular Design**: Clear separation of components for easy customization and scalability.
- **Support for Reinforcement Learning**: Implementations of popular RL algorithms for training AI agents.
- **Natural Language Processing**: Language-based interfaces for specifying tasks and receiving feedback.
- **Extensibility**: Built-in support for custom environments and agents.

## Project Structure

This repository includes the following key components:

### AI
- `agent.py`: Defines the core AI agent. This file contains the logic for interacting with the environment, learning from feedback, and making decisions based on the trained policy.
- `model.py`: Contains the neural network models used by the AI agent for learning and decision-making. Includes pre-built architectures as well as support for custom model definitions.

### Environments
- `environment.py`: Implements the simulation environments where the AI agents operate. It provides the interface for defining new environments or extending existing ones.
- `task_manager.py`: Manages tasks and objectives for agents, ensuring they are evaluated based on specific goals and metrics.

### Utilities
- `config.py`: Contains configuration settings for the project, including hyperparameters for training, paths for saving models, and logging options.
- `logger.py`: Implements logging functionality to track the progress of training and performance metrics.

### Training and Evaluation
- `train.py`: The main script for training AI agents using reinforcement learning techniques. It supports various algorithms, including DQN, PPO, and A3C.
- `evaluate.py`: A script for evaluating the performance of trained models in different environments.

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
   python AI/train.py
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
