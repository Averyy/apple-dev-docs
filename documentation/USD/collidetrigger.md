# CollideTrigger

**Framework**: USD

A trigger that activates when specified objects collide.

#### Overview

The runtime fires this trigger when any of the prims in the list of [`affectedObjects`](affectedobjects.md) collide with any of the prims in [`colliders`](colliders.md).

If all objects can collide with each other, define [`affectedObjects`](affectedobjects.md) and [`colliders`](colliders.md) as the same list.

##### Declaration

```other
class Preliminary_Trigger "CollideTrigger"
```

## Topics

### Properties
- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [colliders](colliders.md)
  A list of prims that interact with objects to create a collision.

## See Also

- [Preliminary_Trigger](preliminary-trigger.md)
  A condition that, when met, performs an action.
- [ProximityToCameraTrigger](proximitytocameratrigger.md)
  A trigger that fires when the camera crosses the distance threshold of an object.
- [SceneTransitionTrigger](scenetransitiontrigger.md)
  A trigger that fires during scene transitions.
- [TapGestureTrigger](tapgesturetrigger.md)
  A trigger that fires when the user taps.
- [NotificationTrigger](notificationtrigger.md)
  A trigger that fires when an app posts a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/collidetrigger)*