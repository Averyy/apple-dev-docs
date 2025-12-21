# exclusive

**Framework**: USD

A Boolean value that determines if a behavior executes exclusively.

#### Overview

The default value is `false`, which indicates that other behaviors’ actions run concurrently with the behavior. If the value is `true`, other exclusive behaviors stop performing actions when the runtime actives a trigger in the behavior.

##### Declaration

```other
uniform bool exclusive = false
```

## See Also

- [triggers](triggers.md)
  A list of prims that execute a behavior’s actions.
- [actions](actions.md)
  A list of actions that make up the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/exclusive)*