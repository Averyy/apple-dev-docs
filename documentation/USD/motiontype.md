# motionType

**Framework**: USD

An option that determines how the action displays or hides a prim.

#### Overview

The action applies this motion to each prim in the list of [`affectedObjects`](affectedobjects.md).

The default value is blank. You need to define a value for this property.

##### Motion Types

- **`none`**: Doesn’t move the prim.
- **`moveLeft`**: Moves the prim in from the left when displaying, and moves the prim to the left when hiding.
- **`moveRight`**: Moves the prim in from the right when displaying, and moves the prim to the right when hiding.
- **`moveFront`**: Moves the prim in from the front when displaying, and moves the prim to the front when hiding.
- **`moveBack`**: Moves the prim in from the back when displaying, and moves the prim to the back when hiding.
- **`moveAbove`**: Moves the prim in from above when displaying, and moves the prim up when hiding.
- **`moveBelow`**: Moves the prim in from below when displaying and moves the prim below when hiding.
- **`pop`**: Scales the prim up from 0% to 100% when displaying, and scales the prim down from 100% to 0% when hiding.
- **`scaleUp`**: Scales the prim up from 0% to 100% before returning back down to 0%.
- **`scaleDown`**: Scales the prim down from a larger size to 100%, then scales the prim up from 100% to a larger size.

##### Declaration

```other
uniform token motionType (
    allowedTokens = ["none", "moveLeft", "moveRight", "moveFront", 
        "moveBack", "moveAbove", "moveBelow", "pop", "scaleUp", "scaleDown"]
)
```

## See Also

- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [duration](duration.md)
  The amount of time that the objects face the camera.
- [style](style.md)
  An option that implements different kinds of animation timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/motiontype)*