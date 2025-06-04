# sessionIdentifier

**Framework**: Watchkit  
**Kind**: property

The identifier for the triggering background transfer.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var sessionIdentifier: String { get }
```

## Overview

This property holds the background session identifier from the [`URLSessionConfiguration`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration) object used to create the background transfer. Use this identifier to create a configuration and session object to connect to the background session task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask/sessionidentifier)*