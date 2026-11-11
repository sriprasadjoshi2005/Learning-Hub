---
title: Rational Agents and Agent Architectures
level: intermediate
---

An intelligent agent must do more than simply react to its environment. It should select actions that help achieve its objectives.

A rational agent chooses actions expected to maximize its performance measure, considering its percept history, available knowledge, and computational limitations.

Rationality is one of the central concepts in Artificial Intelligence.

## 1. Meaning of Rationality

A rational agent selects the action expected to produce the best outcome according to its performance measure.

Rationality does not mean that the agent always knows the correct answer or achieves a perfect result.

Instead, it means that the agent makes the best decision possible using the information and resources available to it.

Example:

A navigation system may recommend a longer route because the shortest route has heavy traffic.

The recommendation can still be rational because it is expected to minimize overall travel time.

## 2. Factors Affecting Rationality

The rationality of an agent depends on four important factors.

**Performance Measure:** Defines how the agent's success is evaluated.

**Percept Sequence:** Contains the observations received by the agent.

**Prior Knowledge:** Includes information about the environment and its behaviour.

**Available Actions:** Represents the actions the agent can perform.

A rational agent selects an action based on these factors.

## 3. Rationality and Omniscience

Rationality and omniscience are different concepts.

**Rationality:** Selecting the best expected action using available information.

**Omniscience:** Knowing the actual outcome of every possible action in advance.

A rational agent is not expected to be omniscient.

Example:

A delivery robot selects a route based on available traffic information. An unexpected road closure occurs after the decision.

The original decision may still have been rational because the robot could not predict the unexpected event.

## 4. Autonomy in Intelligent Agents

An autonomous agent relies on its own experience and observations rather than depending entirely on predefined instructions.

A completely non-autonomous system follows fixed instructions without adapting its behaviour.

Autonomous agents may:
- Learn from previous experiences.
- Update internal knowledge.
- Adapt to environmental changes.
- Improve decision-making strategies.

Autonomy is particularly important in complex environments where every possible situation cannot be programmed in advance.

## 5. Types of Agent Architectures

Different intelligent agents use different methods to select actions.

### Simple Reflex Agents

A simple reflex agent selects actions using condition-action rules.

The general form is:

IF condition THEN action

Example:

IF obstacle detected THEN stop.

Characteristics:
- Uses current percept information.
- Does not require a detailed history of previous percepts.
- Has a simple implementation.
- Works best in fully observable environments.

Limitation:

It may fail when the current percept does not contain enough information to determine the correct action.

### Model-Based Reflex Agents

A model-based reflex agent maintains an internal state representing important aspects of the environment.

It uses:
- Current percepts.
- Previous internal state.
- Knowledge about how the environment changes.
- Knowledge about how actions affect the environment.

Example:

A robot remembers that an obstacle was detected in a previous location, even when the obstacle is temporarily outside its camera view.

This helps it operate in partially observable environments.

### Goal-Based Agents

A goal-based agent selects actions by considering whether they help achieve a specified goal.

Example:

A navigation agent has the goal of reaching a destination.

It evaluates possible movements and chooses actions that move it closer to the destination.

Goal-based agents may use search and planning algorithms.

### Utility-Based Agents

A utility-based agent evaluates possible outcomes using a utility function.

A utility function assigns numerical values representing the desirability of different states or outcomes.

Example:

A navigation system may evaluate routes based on:
- Travel time.
- Fuel consumption.
- Safety.
- Toll charges.

The system can select a route that provides the highest overall utility rather than merely reaching the destination.

### Learning Agents

A learning agent improves its performance through experience.

It can modify its behaviour based on feedback from the environment.

A learning agent generally contains four conceptual components:

**Performance Element:** Selects external actions.

**Learning Element:** Improves the performance element.

**Critic:** Evaluates how well the agent is performing.

**Problem Generator:** Suggests exploratory actions that may produce useful new experiences.

## 6. Comparison of Agent Types

| Agent type | Main mechanism | Important feature |
|---|---|---|
| Simple reflex | Condition-action rules | Reacts to current percept |
| Model-based reflex | Internal state and rules | Maintains environmental information |
| Goal-based | Goal-directed search | Considers desired outcomes |
| Utility-based | Utility function | Compares outcome desirability |
| Learning agent | Experience and feedback | Improves performance |

## 7. Agent Architecture and Intelligent Behaviour

Agent architecture determines how the agent program interacts with its environment.

A suitable architecture depends on:
- The complexity of the task.
- The observability of the environment.
- The available computational resources.
- The required response time.
- The need for learning and adaptation.

Simple environments may require only reflex agents, whereas complicated environments may require planning, utility evaluation, and learning.

## 8. Example: Designing a Smart Vacuum Cleaner

Consider a vacuum cleaner operating in a house.

A simple reflex design may use the rule:

IF dirt detected THEN clean.

A model-based design may remember previously visited areas.

A goal-based design may attempt to clean every accessible room.

A utility-based design may balance cleanliness, battery usage, and cleaning time.

A learning-based design may improve its cleaning route using experience from previous cleaning sessions.

The same task can therefore be approached using different agent architectures.

## Common Exam Traps

- Rationality means maximizing expected performance, not guaranteeing perfect outcomes.
- Rational agents are not necessarily omniscient.
- Simple reflex agents primarily use current percepts.
- Model-based agents maintain internal states.
- Goal-based agents evaluate actions in relation to goals.
- Utility-based agents compare the desirability of possible outcomes.
- Learning agents improve through experience.
- A utility function provides a numerical measure of desirability.

## Quiz

1. What is the primary objective of a rational agent?

- [ ] To know every possible future outcome.
- [ ] To execute the same action in every situation.
- [x] To select actions that maximize expected performance.
- [ ] To avoid interacting with its environment.

> A rational agent chooses actions expected to produce the best performance according to its available information.

2. Which agent architecture maintains an internal representation of the environment?

- [ ] Simple reflex agent.
- [x] Model-based reflex agent.
- [ ] Pure condition-action agent.
- [ ] Random agent.

> A model-based reflex agent maintains internal state information to handle incomplete observations.

3. Which component of a learning agent evaluates its performance?

- [ ] Problem generator.
- [ ] Actuator.
- [x] Critic.
- [ ] Sensor.

> The critic evaluates the agent's behaviour and provides feedback to guide learning.