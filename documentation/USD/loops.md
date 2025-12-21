# loops

**Framework**: USD

A Boolean value indicating whether the group loops.

#### Overview

The default value is `false`, in which the group executes its actions [`performCount`](performcount.md) number of times and then stops.

When `true` and [`type`](type.md) is `serial`, the group restarts its action sequence with the first action after the last action completes. When [`type`](type.md) is `parallel`, the runtime repeats each action independently.

##### Declaration

```other
uniform bool loops = false
```

## See Also

- [info:id](info-id.md)
  The action’s unique identifier.
- [type](type.md)
  An option that controls the order in which the actions execute.
- [performCount](performcount.md)
  A value that specifies the number of times the group’s actions repeat.
- [actions](actions.md)
  A list of actions that make up the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/loops)*