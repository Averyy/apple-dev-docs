# WorkoutKit

**Framework**: Workoutkit  
**Kind**: module

Create, preview, and sync workout compositions to the Workout app.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- watchOS 10.0+

#### Overview

The WorkoutKit framework provides models and utilities for creating and previewing workouts in your iOS and watchOS apps, and for syncing scheduled workouts to the Workout app on Apple Watch. The framework supports the following types of workouts:

You define a workout by initializing one of these workout types. Then you use the workout to create a [`WorkoutPlan`](workoutplan.md), which provides methods for previewing, syncing, or exporting the plan. To open the plan in Workout on Apple Watch, call [`openInWorkoutApp()`](workoutplan/openinworkoutapp().md). To export the plan, call the `dataRepresentation(as:)` method.

You can also use WorkoutKit to create and maintain a workout schedule and, with the user’s permission, sync scheduled compositions to Apple Watch. These compositions appear in a dedicated space in the Workout app and include your app’s icon and name.

Before you can schedule a workout, you must ask for permission. Get the shared [`WorkoutScheduler`](workoutscheduler.md) instance, and call its [`requestAuthorization()`](workoutscheduler/requestauthorization().md) method. Then call the [`schedule(_:at:)`](workoutscheduler/schedule(_:at:).md) method to schedule workouts.

To access health data for the workout, see the [`HealthKit`](https://developer.apple.com/documentation/HealthKit) framework.

## Topics

### Essentials
- [Customizing workouts with WorkoutKit](customizing-workouts-with-workoutkit.md)
  Create, preview, and sync workouts for use in the Workout app on Apple Watch.
### Common workouts
- [struct SingleGoalWorkout](singlegoalworkout.md)
  A workout with a single goal.
- [struct PacerWorkout](pacerworkout.md)
  A workout in which a person covers a specific distance in a given time.
- [struct SwimBikeRunWorkout](swimbikerunworkout.md)
  A workout for multisport activities that include running, biking, and swimming.
### Custom interval workouts
- [struct CustomWorkout](customworkout.md)
  A workout that includes a repeating series of work and recovery steps.
- [struct WorkoutStep](workoutstep.md)
  A step in a workout.
- [struct IntervalBlock](intervalblock.md)
  Blocks of work and recovery steps that repeat in a custom workout.
- [struct IntervalStep](intervalstep.md)
  An interval that represents a work or recovery step in a workout.
- [enum WorkoutGoal](workoutgoal.md)
  A value that specifies the goal for a workout.
- [protocol WorkoutAlert](workoutalert.md)
  An alert that notifies the user of significant events during a workout.
### Workout plans and schedules
- [struct WorkoutPlan](workoutplan.md)
  A wrapper around a workout object that your app can use to open the object in Workout or schedule it for later.
- [struct ScheduledWorkoutPlan](scheduledworkoutplan.md)
  A wrapper around a workout plan that your app can use to schedule the workout plan.
- [class WorkoutScheduler](workoutscheduler.md)
  An object for scheduling and managing workouts.
### Errors
- [enum StateError](stateerror.md)
  An error that occurs while previewing a workout composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WorkoutKit)*