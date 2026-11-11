---
title: Machine Learning Fundamentals
level: intermediate
---

Machine Learning (ML) is a branch of Artificial Intelligence that enables computer systems to learn patterns from data and improve their performance without requiring every decision rule to be explicitly programmed.

Machine learning is widely used in recommendation systems, fraud detection, medical analysis, image recognition, forecasting, speech processing, and many other applications.

## 1. Meaning of Machine Learning

Machine Learning involves developing algorithms that identify patterns in data and use those patterns to make predictions or decisions.

Example:

A system can be trained using thousands of labelled photographs of cats and dogs.

After learning patterns from these examples, the system can classify a new photograph as likely containing a cat or a dog.

The system learns a model from examples instead of relying entirely on manually written classification rules.

## 2. Relationship Between AI, Machine Learning, and Deep Learning

These concepts are related through a hierarchical relationship.

**Artificial Intelligence:** The broader field of developing systems that perform intelligent tasks.

**Machine Learning:** A subset of AI that focuses on learning patterns from data.

**Deep Learning:** A subset of machine learning that uses multilayer neural networks.

Relationship:

Artificial Intelligence → Machine Learning → Deep Learning

Not every AI system uses machine learning, and not every machine learning system uses deep learning.

## 3. How Machine Learning Works

A typical machine learning workflow includes:

1. Collect relevant data.
2. Clean and prepare the data.
3. Select useful features.
4. Choose an appropriate learning algorithm.
5. Train the model.
6. Evaluate its performance.
7. Improve the model if necessary.
8. Deploy the trained model for practical use.
9. Monitor performance over time.

The exact workflow depends on the problem and learning method.

## 4. Important Machine Learning Terminology

**Dataset:** A collection of examples used for training, validation, or testing.

**Sample:** One individual observation in a dataset.

**Feature:** An input variable used by a model.

**Label:** The expected output associated with an example in supervised learning.

**Model:** A learned mathematical or computational representation.

**Training:** The process of adjusting a model using data.

**Prediction:** An output produced by a trained model.

**Parameter:** A value learned by the model during training.

**Hyperparameter:** A configuration value selected before or during model training, such as learning rate or tree depth.

**Loss Function:** Measures how far model predictions are from desired outputs.

## 5. Major Types of Machine Learning

Machine learning is commonly divided into four major categories.

### Supervised Learning

Supervised learning trains a model using labelled examples.

Each training example contains input data and an expected output.

The model learns a relationship between inputs and outputs.

Examples:
- Predicting house prices.
- Classifying emails as spam or non-spam.
- Identifying objects in images.
- Predicting customer demand.

Two major supervised learning tasks are:

**Classification:** Predicts a category or class.

Example: Classifying a message as spam or legitimate.

**Regression:** Predicts a continuous numerical value.

Example: Predicting the price of a house.

### Unsupervised Learning

Unsupervised learning uses data without predefined target labels.

The algorithm attempts to identify hidden patterns, structures, or relationships.

Examples:
- Customer segmentation.
- Grouping similar documents.
- Discovering patterns in biological data.
- Detecting unusual observations.

Common tasks include:

**Clustering:** Groups similar observations.

**Dimensionality Reduction:** Reduces the number of variables while attempting to preserve important information.

### Semi-Supervised Learning

Semi-supervised learning combines a small amount of labelled data with a larger amount of unlabelled data.

It is useful when obtaining labelled examples is expensive or time-consuming.

Example:

A medical image classification system may have a small collection of images labelled by specialists and a much larger collection without labels.

### Reinforcement Learning

Reinforcement Learning (RL) involves an agent interacting with an environment and learning through rewards and penalties.

Important components include:

- Agent.
- Environment.
- State.
- Action.
- Reward.
- Policy.

The agent selects actions and receives feedback based on the consequences.

The objective is generally to maximize cumulative reward over time.

Examples:
- Game-playing agents.
- Robotic control.
- Autonomous navigation research.
- Resource allocation.

## 6. Training, Validation, and Testing Data

Machine learning datasets are often divided into three parts.

**Training Set:** Used to learn model parameters.

**Validation Set:** Used to compare models and tune hyperparameters.

**Test Set:** Used to evaluate the final model on data not used for training or model selection.

Example:

Suppose a dataset contains 10,000 observations.

A possible division is:

- Training: 70%.
- Validation: 15%.
- Testing: 15%.

These proportions are examples rather than universal requirements.

The correct division depends on dataset size, problem type, and experimental design.

## 7. Overfitting and Underfitting

**Overfitting** occurs when a model learns the training data too closely, including noise or accidental patterns.

An overfitted model may perform very well on training data but poorly on unseen data.

**Underfitting** occurs when a model is too simple to capture important patterns in the data.

An underfitted model performs poorly on both training and unseen data.

**Good Generalization** occurs when a model performs effectively on new observations from the intended data distribution.

A common objective is to balance model complexity and generalization.

## 8. Bias and Variance

Bias and variance are important concepts in understanding prediction errors.

**Bias:** Error caused by overly restrictive assumptions in a model.

High bias can lead to underfitting.

**Variance:** Sensitivity of a model to changes in the training dataset.

High variance can lead to overfitting.

The bias-variance trade-off describes the challenge of balancing these two sources of error.

A model should be sufficiently flexible to learn useful patterns without becoming excessively sensitive to individual training examples.

## 9. Common Machine Learning Algorithms

**Linear Regression:** Predicts continuous numerical outputs using a linear relationship.

**Logistic Regression:** Commonly used for classification by modelling class probabilities.

**Decision Trees:** Make predictions using a sequence of feature-based decisions.

**K-Nearest Neighbours (KNN):** Predicts outputs using nearby training examples.

**Support Vector Machines (SVM):** Find decision boundaries that separate classes or support regression.

**Naive Bayes:** Uses probabilistic reasoning based on Bayes' theorem and conditional independence assumptions.

**K-Means Clustering:** Groups observations into a predefined number of clusters.

**Random Forest:** Combines multiple decision trees to improve predictive performance.

These algorithms are selected according to the problem, dataset, and performance requirements.

## 10. Model Evaluation

A model must be evaluated using appropriate metrics.

For classification:

**Accuracy:** Proportion of correctly classified observations.

Accuracy = Correct Predictions / Total Predictions

**Precision:** Proportion of predicted positive cases that are actually positive.

Precision = True Positives / (True Positives + False Positives)

**Recall:** Proportion of actual positive cases correctly identified.

Recall = True Positives / (True Positives + False Negatives)

**F1-Score:** Harmonic mean of precision and recall.

F1 = 2 × Precision × Recall / (Precision + Recall)

For regression:

**Mean Absolute Error (MAE):** Average absolute difference between predicted and actual values.

**Mean Squared Error (MSE):** Average squared prediction error.

**Root Mean Squared Error (RMSE):** Square root of mean squared error.

The choice of metric depends on the task and the consequences of different prediction errors.

## 11. Data Preprocessing

Real-world data often contains problems that must be addressed before training.

Common preprocessing operations include:

**Handling Missing Values:** Removing or estimating missing observations.

**Removing Duplicates:** Identifying repeated records.

**Feature Scaling:** Adjusting numerical variables to comparable scales.

**Encoding Categorical Variables:** Converting categories into numerical representations.

**Outlier Treatment:** Investigating unusually large or small observations.

**Data Splitting:** Separating training, validation, and testing data appropriately.

Preprocessing should be designed carefully to prevent information leakage.

## 12. Data Leakage

Data leakage occurs when information that would not legitimately be available during prediction is used during model training or evaluation.

Example:

Suppose a model predicts whether a patient will develop a condition in the future.

If a feature contains information recorded only after the condition develops, the model may appear highly accurate during evaluation but fail in practical use.

A common prevention method is to perform data splitting before fitting preprocessing operations that learn information from the dataset.

## 13. Applications of Machine Learning

| Field | Application |
|---|---|
| Healthcare | Disease risk prediction |
| Banking | Fraud detection |
| Education | Personalized learning |
| Retail | Product recommendations |
| Transportation | Traffic forecasting |
| Agriculture | Crop yield prediction |
| Cybersecurity | Anomaly detection |
| Entertainment | Content recommendation |
| Manufacturing | Predictive maintenance |

## 14. Further Areas of Machine Learning and Artificial Intelligence

The fundamentals of machine learning lead into several advanced areas. The following concepts provide an overview of the major techniques and developments in modern AI.

### Supervised Learning Algorithms

Supervised learning includes several important algorithms.

- **Linear Regression:** Predicts numerical values using relationships between variables.
- **Logistic Regression:** Performs classification by estimating class probabilities.
- **Decision Trees:** Make predictions through hierarchical feature-based decisions.
- **Random Forests:** Combine multiple decision trees to improve predictive performance.
- **K-Nearest Neighbours:** Predicts outputs using nearby training examples.
- **Support Vector Machines:** Identify decision boundaries that separate classes.
- **Naive Bayes:** Uses probability theory for classification.

### Advanced Classification and Regression

Classification can involve two classes or multiple classes.

Regression can use linear, polynomial, and regularized models to represent different relationships between variables.

Important concepts include:
- Binary and multiclass classification.
- Multilabel classification.
- Polynomial regression.
- Regularization using L1 and L2 penalties.
- Cross-validation for model evaluation.
- Hyperparameter optimization.

### Unsupervised Learning

Unsupervised learning discovers structures in unlabelled data.

Important techniques include:

- **K-Means:** Divides observations into a specified number of clusters.
- **Hierarchical Clustering:** Creates a hierarchy of groups.
- **DBSCAN:** Identifies dense clusters and can detect outliers.
- **Principal Component Analysis (PCA):** Reduces dimensionality while preserving important variation.
- **Anomaly Detection:** Identifies observations that differ significantly from normal patterns.

### Reinforcement Learning

Reinforcement learning trains agents through interaction with an environment.

Important concepts include:

- States and actions.
- Rewards and cumulative rewards.
- Policies and value functions.
- Exploration and exploitation.
- Q-Learning.
- Deep Reinforcement Learning.

An agent learns a strategy that attempts to maximize long-term cumulative reward.

### Artificial Neural Networks

Artificial Neural Networks (ANNs) are computational models inspired by simplified representations of biological neurons.

A basic neural network contains:

- Input layer.
- One or more hidden layers.
- Output layer.
- Weights and biases.
- Activation functions.

During training, the network adjusts its parameters to reduce prediction errors.

Important concepts include:
- Forward propagation.
- Backpropagation.
- Gradient descent.
- Learning rate.
- Activation functions such as ReLU, sigmoid, and tanh.

### Deep Learning

Deep learning uses neural networks with multiple layers to learn increasingly complex representations.

Major architectures include:

- **Convolutional Neural Networks (CNNs):** Commonly used for image processing and computer vision.
- **Recurrent Neural Networks (RNNs):** Designed to process sequential information.
- **Long Short-Term Memory Networks (LSTMs):** A type of RNN designed to capture longer-term dependencies.
- **Transformers:** Use attention mechanisms to process relationships between elements in sequences.

Deep learning is widely applied to image recognition, speech processing, language modelling, and generative AI.

### Natural Language Processing

Natural Language Processing enables computers to process and generate human language.

Major tasks include:
- Tokenization.
- Text classification.
- Sentiment analysis.
- Machine translation.
- Named entity recognition.
- Text summarization.
- Question answering.
- Language generation.

Modern NLP systems frequently use transformer-based language models.

### Computer Vision

Computer vision enables machines to interpret visual information.

Important tasks include:
- Image classification.
- Object detection.
- Image segmentation.
- Facial recognition.
- Optical character recognition.
- Video analysis.

CNNs and vision transformers are among the architectures used in modern computer vision.

### Generative Artificial Intelligence

Generative AI creates new content based on patterns learned from training data.

It can generate:
- Text.
- Images.
- Audio.
- Video.
- Computer code.

Important approaches include:
- Generative Adversarial Networks (GANs).
- Variational Autoencoders (VAEs).
- Diffusion Models.
- Transformer-based generative models.
- Large Language Models (LLMs).

Large Language Models generate text by learning statistical relationships between language tokens and predicting subsequent tokens.

### AI Ethics, Safety and Responsible Development

The development of AI introduces important technical and social considerations.

- **Fairness:** Reducing unjustified discrimination and biased outcomes.
- **Privacy:** Protecting personal and sensitive information.
- **Explainability:** Making model decisions easier to understand.
- **Transparency:** Communicating how AI systems operate and what their limitations are.
- **Reliability:** Ensuring systems behave consistently under appropriate conditions.
- **Security:** Protecting AI systems against attacks and misuse.
- **Accountability:** Establishing responsibility for AI-related decisions and consequences.
- **Human Oversight:** Ensuring appropriate human involvement in important decisions.

### Final Perspective

Artificial Intelligence combines algorithms, data, mathematical reasoning, computational models, and intelligent decision-making.

Computer Science provides the foundations through programming, data structures, algorithms, databases, operating systems, and networks. Artificial Intelligence builds upon these foundations through search, reasoning, machine learning, neural networks, and intelligent agents.

Understanding these connections provides a foundation for exploring advanced AI research and practical applications.

## Common Exam Traps

- Machine learning is a subset of Artificial Intelligence.
- Deep learning is a subset of machine learning.
- Supervised learning uses labelled data.
- Unsupervised learning identifies patterns without predefined target labels.
- Classification predicts categories.
- Regression predicts numerical values.
- Reinforcement learning uses rewards and interaction with an environment.
- Training data is used to learn model parameters.
- Validation data supports model selection and tuning.
- Test data evaluates final performance.
- Overfitting means poor generalization despite strong training performance.
- Data leakage can produce misleading evaluation results.

## Quiz

1. Which type of machine learning uses labelled training examples?

- [ ] Unsupervised learning.
- [x] Supervised learning.
- [ ] Reinforcement learning.
- [ ] Random search.

> Supervised learning uses input examples paired with expected outputs to learn a predictive relationship.

2. Which learning task predicts a continuous numerical value?

- [ ] Classification.
- [ ] Clustering.
- [x] Regression.
- [ ] Association rule mining.

> Regression predicts numerical values such as prices, temperatures, and quantities.

3. What is overfitting?

- [ ] A model that cannot learn any patterns from training data.
- [ ] A model that performs equally poorly on every dataset.
- [x] A model that learns training data too closely and generalizes poorly to unseen data.
- [ ] A model that does not use any input features.

> Overfitting occurs when a model captures noise or overly specific patterns in its training data, reducing its ability to generalize.