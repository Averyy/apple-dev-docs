# Actions and triggers

**Framework**: USD

Enable visual and audible responses to programmatic or environmental events.

#### Overview

Create a `Preliminary_Behavior` to uniquely pair triggers with actions. You can configure some of the triggers and actions, like the settings for a proximity trigger, the velocity of an impulse action, and the audio file for background music or sound effects.

The runtime implements the concrete triggers and actions the schemas define. The exception is `NotificationAction`, which refers to custom effects that an app implements.

## Topics

### Essentials
- [Preliminary_Behavior](preliminary-behavior.md)
  A typed schema that combines one or more triggers with associated actions.
### Triggers
- [Preliminary_Trigger](preliminary-trigger.md)
  A condition that, when met, performs an action.
- [CollideTrigger](collidetrigger.md)
  A trigger that activates when specified objects collide.
- [ProximityToCameraTrigger](proximitytocameratrigger.md)
  A trigger that fires when the camera crosses the distance threshold of an object.
- [SceneTransitionTrigger](scenetransitiontrigger.md)
  A trigger that fires during scene transitions.
- [TapGestureTrigger](tapgesturetrigger.md)
  A trigger that fires when the user taps.
- [NotificationTrigger](notificationtrigger.md)
  A trigger that fires when an app posts a notification.
### Actions
- [Preliminary_Action](preliminary-action.md)
  A specific task that a trigger performs.
- [AudioAction](audioaction.md)
  An action that plays audio.
- [ChangeSceneAction](changesceneaction.md)
  An action that transitions from one scene to another.
- [EmphasizeAction](emphasizeaction.md)
  An action that performs an animation to call attention to an object.
- [GroupAction](groupaction.md)
  An action that runs a list of other actions.
- [ImpulseAction](impulseaction.md)
  An action that adds velocity to an prim.
- [LookAtCameraAction](lookatcameraaction.md)
  An action that reorients an object to face the user’s camera.
- [OrbitAction](orbitaction.md)
  An action that orbits a set of prims around another.
- [SpinAction](spinaction.md)
  An action that spins a prim.
- [StartAnimationAction](startanimationaction.md)
  An action that plays an asset’s animation.
- [TransformAction](transformaction.md)
  An action that animates from one transform to another.
- [TransformAnimationAction](transformanimationaction.md)
  An action that plays a transform animation.
- [VisibilityAction](visibilityaction.md)
  An action that displays or hides objects over a period of time.
- [WaitAction](waitaction.md)
  An action that performs a delay.
- [NotificationAction](notificationaction.md)
  An action that sends a custom notification to an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/actions-and-triggers)*