# kDNSServiceFlagsShareConnection

**Framework**: dnssd  
**Kind**: var

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var kDNSServiceFlagsShareConnection: UInt32 { get }
```

#### Discussion

For efficiency, clients that perform many concurrent operations may want to use a single Unix Domain Socket connection with the background daemon, instead of having a separate connection for each independent operation. To use this mode, clients first call DNSServiceCreateConnection(&MainRef) to initialize the main DNSServiceRef. For each subsequent operation that is to share that same connection, the client copies the MainRef, and then passes the address of that copy, setting the ShareConnection flag to tell the library that this DNSServiceRef is not a typical uninitialized DNSServiceRef; it’s a copy of an existing DNSServiceRef whose connection information should be reused.

For example:

```objc
 
 DNSServiceErrorType error;
 DNSServiceRef MainRef;
 error = DNSServiceCreateConnection(&MainRef);
 if (error) ...
 DNSServiceRef BrowseRef = MainRef;  // Important: COPY the primary DNSServiceRef first...
 error = DNSServiceBrowse(&BrowseRef, kDNSServiceFlagsShareConnection, ...); // then use the copy
 if (error) ...
 ...
 DNSServiceRefDeallocate(BrowseRef); // Terminate the browse operation
 DNSServiceRefDeallocate(MainRef);   // Terminate the shared connection
 
```

Notes:

1. Collective [`kDNSServiceFlagsMoreComing`](kdnsserviceflagsmorecoming.md) flag When callbacks are invoked using a shared DNSServiceRef, the [`kDNSServiceFlagsMoreComing`](kdnsserviceflagsmorecoming.md) flag applies collectively to *all* active operations sharing the same parent DNSServiceRef. If the MoreComing flag is set it means that there are more results queued on this parent DNSServiceRef, but not necessarily more results for this particular callback function. The implication of this for client programmers is that when a callback is invoked with the MoreComing flag set, the code should update its internal data structures with the new result, and set a variable indicating that its UI needs to be updated. Then, later when a callback is eventually invoked with the MoreComing flag not set, the code should update *all* stale UI elements related to that shared parent DNSServiceRef that need updating, not just the UI elements related to the particular callback that happened to be the last one to be invoked.
2. Canceling operations and [`kDNSServiceFlagsMoreComing`](kdnsserviceflagsmorecoming.md) Whenever you cancel any operation for which you had deferred UI updates waiting because of a [`kDNSServiceFlagsMoreComing`](kdnsserviceflagsmorecoming.md) flag, you should perform those deferred UI updates. This is because, after cancelling the operation, you can no longer wait for a callback *without* MoreComing set, to tell you do perform your deferred UI updates (the operation has been canceled, so there will be no more callbacks). An implication of the collective [`kDNSServiceFlagsMoreComing`](kdnsserviceflagsmorecoming.md) flag for shared connections is that this guideline applies more broadly – any time you cancel an operation on a shared connection, you should perform all deferred UI updates for all operations sharing that connection. This is because the MoreComing flag might have been referring to events coming for the operation you canceled, which will now not be coming because the operation has been canceled.
3. Only share DNSServiceRef’s created with DNSServiceCreateConnection Calling DNSServiceCreateConnection(&ref) creates a special shareable DNSServiceRef. DNSServiceRef’s created by other calls like [`DNSServiceBrowse(_:_:_:_:_:_:_:)`](dnsservicebrowse(_:_:_:_:_:_:_:).md) or [`DNSServiceResolve(_:_:_:_:_:_:_:_:)`](dnsserviceresolve(_:_:_:_:_:_:_:_:).md) cannot be shared by copying them and using kDNSServiceFlagsShareConnection.
4. Don’t Double-Deallocate Calling DNSServiceRefDeallocate(ref) for a particular operation’s DNSServiceRef terminates just that operation. Calling DNSServiceRefDeallocate(ref) for the main shared DNSServiceRef (the parent DNSServiceRef, originally created by DNSServiceCreateConnection(&ref)) automatically terminates the shared connection and all operations that were still using it. After doing this, DO NOT then attempt to deallocate any remaining subordinate DNSServiceRef’s. The memory used by those subordinate DNSServiceRef’s has already been freed, so any attempt to do a DNSServiceRefDeallocate (or any other operation) on them will result in accesses to freed memory, leading to crashes or other equally undesirable results.
5. Thread Safety The dns_sd.h API does not presuppose any particular threading model, and consequently does no locking of its own (which would require linking some specific threading library). If client code calls API routines on the same DNSServiceRef concurrently from multiple threads, it is the client’s responsibility to use a mutext lock or take similar appropriate precautions to serialize those calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsshareconnection)*