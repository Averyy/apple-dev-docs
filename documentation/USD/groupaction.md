# GroupAction

**Framework**: USD

An action that runs a list of other actions.

#### Overview

This action defines how the runtime executes each action in the [`actions`](actions.md) array. When [`type`](type.md) is `serial`, the runtime performs [`actions`](actions.md) one after the other. When [`type`](type.md) is `concurrent`, the runtime starts each action at the same time.

When this action’s [`type`](type.md) is `serial`, you can specify a delay between two actions by placing a `WaitAction` between them.

##### Declaration

```other
class Preliminary_Action "GroupAction"
```

##### Create a Sequential or Looping Group Action

The following example defines a group of actions that run sequentially. The group contains a flip action, a wait action, and a hide action.

```other
def Preliminary_Action "SimpleGroup" (
    inherits = </GroupAction>
)
{
    rel actions = [ <Flip>, <Wait>, <Hide> ]
    uniform bool loops = false
    uniform uint performCount = 1

    def Action "Flip" (
        inherits = </EmphasizeAction>
    )
    {
        uniform token motionType = "flip"
    }

    def Action "Wait" (
        inherits = </WaitAction>
    )
    {
    }

    def Action "Hide" (
        inherits = </VisibilityAction>
    )
    {
        uniform token type = "hide"
    }
}
```

The following group named `EndlessLoop` repeats a set of actions indefinitely because `performCount` is `0`.

```swift
def Action "EndlessLoop" (
    inherits = </GroupAction>
)
{
    rel actions = [...]
    uniform bool loops = true
    uniform uint performCount = 0
}
```

## Topics

### Properties
- [info:id](info-id.md)
  The action’s unique identifier.
- [type](type.md)
  An option that controls the order in which the actions execute.
- [loops](loops.md)
  A Boolean value indicating whether the group loops.
- [performCount](performcount.md)
  A value that specifies the number of times the group’s actions repeat.
- [actions](actions.md)
  A list of actions that make up the group.

## See Also

- [Preliminary_Action](preliminary-action.md)
  A specific task that a trigger performs.
- [AudioAction](audioaction.md)
  An action that plays audio.
- [ChangeSceneAction](changesceneaction.md)
  An action that transitions from one scene to another.
- [EmphasizeAction](emphasizeaction.md)
  An action that performs an animation to call attention to an object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/usd/groupaction)*