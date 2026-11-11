---
title: Intelligent Agents and Environments
level: intermediate
---

An intelligent agent is an entity that perceives its environment through sensors and acts upon that environment through actuators to achieve specific objectives.

The concept of intelligent agents is fundamental to Artificial Intelligence because it provides a general framework for understanding how intelligent systems observe situations, make decisions, and perform actions.

## 1. Meaning of an Agent

An agent is anything that can perceive its environment and take actions.

Examples include:
- A human using eyes and ears to observe surroundings and hands to perform actions.
- A robot using cameras and motors.
- A self-driving car using cameras, radar, and steering systems.
- A software assistant receiving user input and producing responses.

An agent does not necessarily need a physical body. Software systems can also act as agents.

## 2. Sensors and Actuators

An agent interacts with its environment through two major components.

**Sensors:** Collect information from the environment.

Examples:
- Cameras.
- Microphones.
- Temperature sensors.
- GPS receivers.
- Touch sensors.
- Software input streams.

**Actuators:** Perform actions that affect the environment.

Examples:
- Wheels and motors.
- Robotic arms.
- Speakers.
- Display systems.
- Software commands.
- Control signals.

The general interaction cycle is:

Environment → Sensors → Agent → Actuators → Environment

The agent receives percepts, processes available information, selects an action, and executes it.

## 3. Percepts and Percept Sequences

A percept is the information an agent receives from its environment at a particular moment.

A percept sequence is the complete history of percepts received by the agent.

Example:

A robot navigating a room may receive the following percepts:

1. A wall is detected ahead.
2. An obstacle is detected on the left.
3. An open path is detected on the right.

The robot uses this information to select an appropriate movement.

The complete percept sequence may help the agent understand how the environment has changed over time.

## 4. Agent Function and Agent Program

An agent function describes the relationship between percept sequences and actions.

It can be represented as:

Action = f(Percept Sequence)

The agent function defines what action should be selected for every possible percept sequence.

An agent program is the actual implementation of this function running on a physical or computational architecture.

Important distinction:

- Agent function: Abstract mathematical description of behaviour.
- Agent program: Executable implementation of that behaviour.
- Architecture: The hardware or software platform on which the agent program operates.

An agent can be represented as:

Agent = Architecture + Agent Program

## 5. Properties of Environments

The environment is the external world in which an agent operates.

AI environments can be classified according to several properties.

**Fully Observable vs Partially Observable**

A fully observable environment provides the agent with all relevant information about the current state.

A partially observable environment provides incomplete or uncertain information.

Example:
- Chess is generally treated as fully observable.
- Driving in heavy fog is partially observable.

**Deterministic vs Stochastic**

A deterministic environment produces predictable results when the current state and action are known.

A stochastic environment involves uncertainty in the outcomes of actions.

Example:
- A simple mathematical puzzle may be deterministic.
- Real-world weather conditions are stochastic.

**Episodic vs Sequential**

In an episodic environment, each task or decision is largely independent of previous tasks.

In a sequential environment, current decisions affect future states and decisions.

Example:
- Classifying independent images is episodic.
- Playing chess is sequential.

**Static vs Dynamic**

A static environment does not change while the agent is deciding.

A dynamic environment may change during the decision-making process.

Example:
- A printed crossword puzzle is static.
- Road traffic is dynamic.

**Discrete vs Continuous**

A discrete environment contains a finite or countable set of states, actions, or percepts.

A continuous environment involves values that can vary over a continuous range.

Example:
- Chess has discrete board positions and moves.
- Robot movement in physical space often involves continuous positions and velocities.

**Single-Agent vs Multi-Agent**

A single-agent environment contains one agent making decisions.

A multi-agent environment contains multiple agents that may cooperate, compete, or interact.

Example:
- Solving a Sudoku puzzle is single-agent.
- Playing football involves multiple interacting agents.

**Known vs Unknown**

A known environment has understood rules governing its behaviour.

An unknown environment requires the agent to learn or discover how it behaves.

## 6. PEAS Representation

PEAS is a framework used to describe an intelligent agent's task environment.

PEAS stands for:

- P: Performance Measure.
- E: Environment.
- A: Actuators.
- S: Sensors.

Each component describes an important aspect of the agent's task.

**Example: Autonomous Taxi**

| Component | Description |
|---|---|
| Performance Measure | Safety, travel time, passenger comfort, legal compliance |
| Environment | Roads, traffic, pedestrians, passengers, weather |
| Actuators | Steering, accelerator, brakes, indicators |
| Sensors | Cameras, GPS, radar, lidar, speed sensors |

**Example: Vacuum-Cleaning Robot**

| Component | Description |
|---|---|
| Performance Measure | Cleanliness, time, energy consumption |
| Environment | Rooms, floors, furniture, obstacles |
| Actuators | Wheels, suction motor, brushes |
| Sensors | Dirt sensors, proximity sensors, cameras |

PEAS helps identify the requirements of an intelligent system before designing it.

## 7. Examples of Intelligent Agents

**Simple Software Agent:** Receives user input and performs a predefined operation.

**Recommendation Agent:** Observes user preferences and recommends relevant content.

**Robotic Agent:** Uses sensors and actuators to interact with physical surroundings.

**Autonomous Vehicle Agent:** Observes traffic conditions and controls vehicle movement.

**Game-Playing Agent:** Analyzes possible moves and selects actions according to a strategy.

## 8. Importance of Intelligent Agents

The agent model provides a common framework for designing different AI systems.

It helps developers:
- Identify required sensors and actuators.
- Understand the operating environment.
- Define performance objectives.
- Design appropriate decision-making mechanisms.
- Evaluate the behaviour of intelligent systems.

## Common Exam Traps

- Sensors receive information; actuators perform actions.
- A percept is a single observation, while a percept sequence is a history of observations.
- An agent program implements an agent function.
- An architecture provides the platform for the agent program.
- PEAS stands for Performance Measure, Environment, Actuators, and Sensors.
- Fully observable does not mean deterministic.
- Dynamic does not necessarily mean stochastic.

## Quiz

1. Which component allows an intelligent agent to perceive its environment?

- [ ] Actuators.
- [x] Sensors.
- [ ] Performance measures.
- [ ] Knowledge bases.

> Sensors collect information from the environment and provide percepts to the agent.

2. What does PEAS stand for?

- [ ] Processing, Execution, Analysis, Storage.
- [ ] Perception, Evaluation, Action, Search.
- [x] Performance Measure, Environment, Actuators, Sensors.
- [ ] Planning, Execution, Architecture, State.

> PEAS is a framework for describing an agent's task environment and requirements.

3. Which environment is generally associated with incomplete or uncertain percept information?

- [ ] Fully observable environment.
- [x] Partially observable environment.
- [ ] Static environment.
- [ ] Episodic environment.

> A partially observable environment does not provide the agent with all relevant information about the current state.