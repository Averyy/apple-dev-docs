# Preliminary_Trigger

**Framework**: USD

A condition that, when met, performs an action.

#### Overview

Because it inherits `Typed`, this schema declares a `Preliminary_Trigger` as a type of prim. For more information about typed schemas, see USD Specification > [`Typed`](https://developer.apple.comhttp://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-TypedSchema).

The runtime executes triggers based on:

- User input, like a user’s tap gesture.
- Scene state, including a prim’s proximity to the user’s device.
- Programmatic conditions, like application state or a function result.

##### Declaration

```other
class "Preliminary_Trigger" (
    inherits = </Typed>
)
```

##### Add a Tap Trigger to a Cube

The following example shows how a prim named `TapCube` opts in to notification of user taps.

```other
#usda 1.0

def Cube "Cube" {}

def Preliminary_Trigger "TapCube" {
    uniform token info:id = "TapGesture"
    rel affectedObjects = [ </Cube> ]
}
```

## Topics

### Properties
- [info:id](info-id.md)
  The action’s unique identifier.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/preliminary-trigger)*