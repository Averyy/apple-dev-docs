# multiplePerformOperation

**Framework**: USD

An option that indicates how an action handles an additional invocation while running.

#### Overview

The runtime doesn’t react to this property for all actions.

##### Additional Invocation Options

- **`allow`**: Restarts the action by playing it over again.
- **`ignore`**: Continues running the current action, ignoring the additional invocation.
- **`stop`**: Stops the current action.

##### Declaration

```other
uniform token multiplePerformOperation= "ignore" (
    allowedTokens = ["ignore", "allow", "stop"]
)
```

## See Also

- [info:id](info-id.md)
  The action’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/multipleperformoperation)*