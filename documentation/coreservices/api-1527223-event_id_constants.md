# Event ID Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify the event ID for an Apple event.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : AEEventID {
    ...
};
```

## Topics

### Constants
- [kAEOpenApplication](./api-1527223-event_id_constants/kaeopenapplication.md)
  Event that launches an application.
- [kAEReopenApplication](./api-1556377-kaeqdnotor/kaereopenapplication.md)
  Event that reopens an application. Sent, for example, when your application is running and a user clicks your application icon in the Dock.
- [kAEOpenDocuments](./api-1527223-event_id_constants/kaeopendocuments.md)
- [kAEPrintDocuments](./api-1527223-event_id_constants/kaeprintdocuments.md)
  Event that provides an application with a list of documents to print.
- [kAEOpenContents](./api-1527223-event_id_constants/kaeopencontents.md)
- [kAEQuitApplication](./api-1527223-event_id_constants/kaequitapplication.md)
  Event that causes the application to quit.
- [kAEAnswer](./api-1527223-event_id_constants/kaeanswer.md)
  Event that is a reply Apple event.
- [kAEApplicationDied](./api-1527223-event_id_constants/kaeapplicationdied.md)
  Event sent by the Process Manager to an application that launched another application when the launched application quits or terminates.
- [kAEShowPreferences](./api-1527223-event_id_constants/kaeshowpreferences.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1527223-event_id_constants)*