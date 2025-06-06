# Event Class Constants

**Framework**: Core Services

Specify the event class for an Apple event.

#### Overview

Apple events are identified by their event class and event ID attributes, each of which specifies an arbitrary four-character code. The event class appears in the `message` field of the event record for an Apple event. For example, certain Apple events that are sent by the Mac OS have the value `'aevt'` in the `message` fields of their event records. This value can be represented with the constant `kCoreEventClass`.

Groups of related Apple events are known as suites. For example, the common events that most applications support are grouped in the Standard Suite. The Standard Suite includes the events of the Core suite (`open application` , `reopen`, `opencontents`, `open documents`, `printdocuments`, and `quit`), as well as such events as `count`, `delete`, and `make`. Suites may use a common event class, but doing so is not required, and does not result in any special treatment by AppleScript or the Apple Event Manager.

AppleScript defines suites that provide terminology for Text, Database, Macintosh Connectivity, and other types of related operations. The terms defined in the AppleScript suite itself make up the largest suite. These terms are global to AppleScript, and are available to your application, even if your `'aete'` resource doesn’t explicitly include them.

## Topics

### Constants
- [var kCoreEventClass: DescType](kcoreeventclass.md)
  An Apple event sent by the Mac OS; applications that present a graphical interface to the user should be able to any events sent by the Mac OS that apply to the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/apple_events/1527210-event_class_constants)*