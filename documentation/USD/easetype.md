# easeType

**Framework**: USD

An option that describes the animation’s change in pace over time.

#### Overview

The default type is `none`, which is synonymous with linear timing.

##### Ease Types

- **`none`**: Paces the action at a constant rate.
- **`in`**: Paces the action slower at the beginning.
- **`out`**: Paces the action slower at the end.
- **`inout`**: Paces the action slower at the beginning and end.

##### Declaration

```other
uniform token easeType = "none"
```

## See Also

- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [xformTarget](xformtarget.md)
  A prim that provides the transform to which this action animates.
- [duration](duration.md)
  The amount of time that the objects face the camera.
- [type](type.md)
  An option that controls the order in which the actions execute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/easetype)*