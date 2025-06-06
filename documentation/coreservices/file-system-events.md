# File System Events

**Framework**: Core Services

Get notifications when the contents of a directory hierarchy change.

#### Overview

The file system events API provides a way for your application to ask for notification when the contents of a directory hierarchy are modified. For example, your application can use this to quickly detect when the user modifies a file within a project bundle using another application.

It also provides a lightweight way to determine whether the contents of a directory hierarchy have changed since your application last examined them. For example, a backup application can use this to determine what files have changed since a given time stamp or a given event ID.

## Topics

### Functions
- [func FSEventStreamCopyDescription(ConstFSEventStreamRef) -> CFString](1442676-fseventstreamcopydescription.md)
- [func FSEventStreamCopyPathsBeingWatched(ConstFSEventStreamRef) -> CFArray](1447917-fseventstreamcopypathsbeingwatch.md)
- [func FSEventStreamCreate(CFAllocator?, FSEventStreamCallback, UnsafeMutablePointer<FSEventStreamContext>?, CFArray, FSEventStreamEventId, CFTimeInterval, FSEventStreamCreateFlags) -> FSEventStreamRef?](1443980-fseventstreamcreate.md)
- [func FSEventStreamCreateRelativeToDevice(CFAllocator?, FSEventStreamCallback, UnsafeMutablePointer<FSEventStreamContext>?, dev_t, CFArray, FSEventStreamEventId, CFTimeInterval, FSEventStreamCreateFlags) -> FSEventStreamRef?](1447341-fseventstreamcreaterelativetodev.md)
- [func FSEventStreamFlushAsync(FSEventStreamRef) -> FSEventStreamEventId](1441727-fseventstreamflushasync.md)
- [func FSEventStreamFlushSync(FSEventStreamRef)](1445629-fseventstreamflushsync.md)
- [func FSEventStreamGetDeviceBeingWatched(ConstFSEventStreamRef) -> dev_t](1449675-fseventstreamgetdevicebeingwatch.md)
- [func FSEventStreamGetLatestEventId(ConstFSEventStreamRef) -> FSEventStreamEventId](1446030-fseventstreamgetlatesteventid.md)
- [func FSEventStreamInvalidate(FSEventStreamRef)](1446990-fseventstreaminvalidate.md)
- [func FSEventStreamRelease(FSEventStreamRef)](1445989-fseventstreamrelease.md)
- [func FSEventStreamRetain(FSEventStreamRef)](1444986-fseventstreamretain.md)
- [func FSEventStreamScheduleWithRunLoop(FSEventStreamRef, CFRunLoop, CFString)](1447824-fseventstreamschedulewithrunloop.md)
- [func FSEventStreamSetDispatchQueue(FSEventStreamRef, dispatch_queue_t?)](1444164-fseventstreamsetdispatchqueue.md)
  Schedules the stream on the specified dispatch queue.
- [func FSEventStreamSetExclusionPaths(FSEventStreamRef, CFArray) -> Bool](1444666-fseventstreamsetexclusionpaths.md)
- [func FSEventStreamShow(ConstFSEventStreamRef)](1444302-fseventstreamshow.md)
- [func FSEventStreamStart(FSEventStreamRef) -> Bool](1448000-fseventstreamstart.md)
- [func FSEventStreamStop(FSEventStreamRef)](1447673-fseventstreamstop.md)
- [func FSEventStreamUnscheduleFromRunLoop(FSEventStreamRef, CFRunLoop, CFString)](1441982-fseventstreamunschedulefromrunlo.md)
- [func FSEventsCopyUUIDForDevice(dev_t) -> CFUUID?](1444453-fseventscopyuuidfordevice.md)
- [func FSEventsGetCurrentEventId() -> FSEventStreamEventId](1442917-fseventsgetcurrenteventid.md)
- [func FSEventsGetLastEventIdForDeviceBeforeTime(dev_t, CFAbsoluteTime) -> FSEventStreamEventId](1449772-fseventsgetlasteventidfordeviceb.md)
- [func FSEventsPurgeEventsForDeviceUpToEventId(dev_t, FSEventStreamEventId) -> Bool](1447985-fseventspurgeeventsfordeviceupto.md)
### Enumerations
- [FSEventStreamCreateFlags](file_system_events/1455376-fseventstreamcreateflags.md)
- [FSEventStreamEventFlags](file_system_events/1455361-fseventstreameventflags.md)
### Data Types
- [typealias FSEventStreamCallback](fseventstreamcallback.md)
- [typealias FSEventStreamCreateFlags](fseventstreamcreateflags.md)
- [typealias FSEventStreamEventFlags](fseventstreameventflags.md)
- [typealias FSEventStreamEventId](fseventstreameventid.md)
- [typealias FSEventStreamRef](fseventstreamref.md)
### Constants
- [var kFSEventStreamEventExtendedDataPathKey: String](kfseventstreameventextendeddatapathkey.md)
- [var kFSEventStreamEventExtendedFileIDKey: String](kfseventstreameventextendedfileidkey.md)

## See Also

- [File System Events Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Darwin/Conceptual/FSEvents_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005289)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_system_events)*