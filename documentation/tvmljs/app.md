# App

**Framework**: TVMLKit JS  
**Kind**: cl  
**Role**: Class

An object that provides access to—and a means to respond to—app life-cycle events.

**Availability**:
- tvOS 9.0+

## Declaration

```
interface App
```

#### Overview

You cannot create an instance of the `App` class. An instance of this class is available in the global context as `App`.

## Topics

### Responding to App Life Cycle Events
- [onError](./app/api-1627353-onerror.md)
  A callback function that is automatically called when an error is sent from the Apple TV.
- [onExit](./app/api-1627419-onexit.md)
  A callback function that is automatically called when the app has been exited.
- [onLaunch](./app/api-1627407-onlaunch.md)
  A callback function that is automatically called when the app has been launched.
- [onResume](./app/api-1627415-onresume.md)
  A callback function that is automatically called when the app moves to the foreground.
- [onSuspend](./app/api-1627431-onsuspend.md)
  A callback function that is automatically called when the app is sent to the background.
### Reloading the App
- [reload](./app/api-1627357-reload.md)
  Reloads the app.
### Instance Properties
- [onDocumentRequest](./app/api-3192095-ondocumentrequest.md)

## See Also

### App Initialization
- [UserDefaults](./userdefaults.md)
  An object that contains the app's default preferences.
- [NavigationDocument](./navigationdocument.md)
  A document stack that holds the individual TVML documents for a client-server app.
- [Responding to User Interaction](./responding_to_user_interaction.md)
  Update onscreen information by adding event listeners to your Apple TV app.
- [EventListenerObject](./eventlistenerobject.md)
  An object that communicates events and allows other objects to add themselves as listeners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/app)*