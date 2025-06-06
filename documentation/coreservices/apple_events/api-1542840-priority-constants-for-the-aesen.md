# Priority Constants for the AESend Function (Deprecated in macOS)

**Framework**: Core Services

Specify a value for the `sendPriority` parameter of the `AESend` function.

#### Overview

For related information, see the `AESend(_:_:_:_:_:_:_:)` function and [`AESendMode`](aesendmode.md). 

##### 1770288

The `sendPriority` parameter of the `AESend` function is deprecated in macOS.

## Topics

### Constants
- [var kAENormalPriority: Int](kaenormalpriority.md)
  The Apple Event Manager posts the event at the end of the event queue of the server process and the server processes the Apple event as soon as it has the opportunity.
- [var kAEHighPriority: Int](kaehighpriority.md)
  The Apple Event Manager posts the event at the beginning of the event queue of the server process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/apple_events/1542840-priority_constants_for_the_aesen)*