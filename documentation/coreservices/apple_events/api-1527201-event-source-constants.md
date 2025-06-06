# Event Source Constants

**Framework**: Core Services

Identify how an Apple event was delivered.

#### Overview

For an example of how you might use these constants with the [`AEGetAttributePtr(_:_:_:_:_:_:_:)`](1445109-aegetattributeptr.md) function, see the data type [`AEEventSource`](aeeventsource.md). 

## Topics

### Constants
- [var kAEUnknownSource: Int](kaeunknownsource.md)
  The source of the Apple event is unknown.
- [var kAEDirectCall: Int](kaedirectcall.md)
  The source of the Apple event is a direct call that bypassed the PPC Toolbox.
- [var kAESameProcess: Int](kaesameprocess.md)
  The source of the Apple event is the same application that received the event (the target application and the source application are the same).
- [var kAELocalProcess: Int](kaelocalprocess.md)
  The source application is another process on the same computer as the target application.
- [var kAERemoteProcess: Int](kaeremoteprocess.md)
  The source application is a process on a remote computer on the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/apple_events/1527201-event_source_constants)*