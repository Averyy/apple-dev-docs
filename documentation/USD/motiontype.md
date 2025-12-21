# motionType

**Framework**: USD

An option that determines how the action displays or hides a prim.

#### Overview

The action applies this motion to each prim in the list of [`affectedObjects`](affectedobjects.md).

The default value is blank. You need to define a value for this property.

##### Motion Types

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