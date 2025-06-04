# focus()

**Framework**: Watchkit  
**Kind**: method

Begins the delivery of crown events to the current crown sequencer.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func focus()
```

## Overview

You must call this method to begin the delivery of crown events to your crown sequencer object. If your interface includes a picker or scrollable scene that is currently receiving crown events, calling this method causes that object to resign focus.

## See Also

- [func resignFocus()](resignfocus().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/resignfocus()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/focus())*