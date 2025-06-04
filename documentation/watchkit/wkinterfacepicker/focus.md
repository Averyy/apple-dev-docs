# focus()

**Framework**: Watchkit  
**Kind**: method

Configures the picker to receive input from the Digital Crown.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func focus()
```

## Overview

The picker adds custom highlighting when it is configured as the target of crown input. For an interface that contains multiple pickers, you might use this method to switch the focus at an appropriate time. Because scrolling in an interface controller causes the picker to lose focus, you can also use this method to select the picker again later.

## See Also

- [func resignFocus()](resignfocus().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/resignfocus()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/focus())*