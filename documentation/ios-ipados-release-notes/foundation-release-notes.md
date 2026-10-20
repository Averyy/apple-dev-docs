# Foundation Release Notes

**Framework**: iOS & iPadOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

#### Overview

Foundation in macOS 10.14, iOS 12, watchOS 5, and tvOS 12 includes new features, API changes, and deprecations. For information about earlier releases, see [Foundation Release Notes for macOS 10.13 and iOS 11](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-Foundation/index.html).

##### Secure Data Archival and Unarchival

The [`NSKeyedArchiver`](../Foundation/nskeyedarchiver.md) and [`NSKeyedUnarchiver`](../Foundation/nskeyedunarchiver.md) classes have new initializers and helper methods that make it easier for you to enable secure coding for archival and unarchival. Each initializer or helper method replaces a corresponding member that’s now deprecated.

- [`init(requiringSecureCoding:)`](../Foundation/nskeyedarchiver/init%28requiringsecurecoding%29.md) replaces [`init()`](../Foundation/nskeyedunarchiver/init%28%29.md) and [`init(forWritingWith:)`](../Foundation/nskeyedarchiver/init%28forwritingwith%29.md).
- [`archivedData(withRootObject:requiringSecureCoding:)`](../Foundation/nskeyedarchiver/archiveddata%28withrootobject,requiringsecurecoding%29.md) replaces [`archivedData(withRootObject:)`](../Foundation/nskeyedarchiver/archiveddata%28withrootobject%29.md) and [`archiveRootObject(_:toFile:)`](../Foundation/nskeyedarchiver/archiverootobject%28_,tofile%29.md).
- [`init(forReadingFrom:)`](../Foundation/nskeyedunarchiver/init%28forreadingfrom%29.md) replaces [`init()`](../Foundation/nskeyedunarchiver/init%28%29.md) and [`init(forReadingWith:)`](../Foundation/nskeyedunarchiver/init%28forreadingwith%29.md).
- [`unarchivedObject(ofClass:from:)`](../Foundation/nskeyedunarchiver/unarchivedobject%28ofclass,from%29.md) and [`unarchivedObject(ofClasses:from:)`](../Foundation/nskeyedunarchiver/unarchivedobject%28ofclasses,from%29-b9t5.md) replace [`unarchiveObject(with:)`](../Foundation/nskeyedunarchiver/unarchiveobject%28with%29.md), [`unarchiveTopLevelObjectWithData(_:)`](../Foundation/nskeyedunarchiver/unarchivetoplevelobjectwithdata%28_%29.md), and [`unarchiveObject(withFile:)`](../Foundation/nskeyedunarchiver/unarchiveobject%28withfile%29.md).

  You use the new [`unarchivedObject(ofClasses:from:)`](../Foundation/nskeyedunarchiver/unarchivedobject%28ofclasses,from%29-b9t5.md) method when unarchiving instances that are subclasses of one of the list of classes you supply. You can use these initializers and helper methods in apps that are compatible with macOS 10.13, iOS 11, watchOS 4, tvOS 11, and subsequent releases of each operating system.

For more information, see the WWDC 2018 session [Data You Can Trust](https://developer.apple.com/videos/play/wwdc2018/222/).

##### Secure Value Transformer

[`NSSecureUnarchiveFromDataTransformer`](../Foundation/nssecureunarchivefromdatatransformer.md) is a new subclass of [`ValueTransformer`](../Foundation/valuetransformer.md). It uses [`NSKeyedArchiver`](../Foundation/nskeyedarchiver.md) and [`NSKeyedUnarchiver`](../Foundation/nskeyedunarchiver.md) to archive and unarchive data by enabling `requiresSecureCoding`.

When unarchiving from [`NSData`](../Foundation/nsdata.md), [`NSSecureUnarchiveFromDataTransformer`](../Foundation/nssecureunarchivefromdatatransformer.md) uses its [`allowedTopLevelClasses`](../Foundation/nssecureunarchivefromdatatransformer/allowedtoplevelclasses.md) list to decode objects by calling the new [`unarchivedObject(ofClasses:from:)`](../Foundation/nskeyedunarchiver/unarchivedobject%28ofclasses,from%29-b9t5.md) method. By default, this list includes all property list types—[`NSArray`](../Foundation/nsarray.md), [`NSDictionary`](../Foundation/nsdictionary.md), [`NSString`](../Foundation/nsstring.md), [`NSNumber`](../Foundation/nsnumber.md), [`NSDate`](../Foundation/nsdate.md), [`NSData`](../Foundation/nsdata.md), and [`NSNull`](../Foundation/nsnull.md)—along with [`NSURL`](../Foundation/nsurl.md) and [`NSUUID`](../Foundation/nsuuid.md).

When archiving to [`NSData`](../Foundation/nsdata.md), this transformer calls the new [`archivedData(withRootObject:requiringSecureCoding:)`](../Foundation/nskeyedarchiver/archiveddata%28withrootobject,requiringsecurecoding%29.md) method and enables requiresSecureCoding.

To transform top-level values of types other than the defaults listed above, subclass [`NSSecureUnarchiveFromDataTransformer`](../Foundation/nssecureunarchivefromdatatransformer.md).

- If you expect to decode a top-level value of only one allowed type, override [`transformedValueClass()`](../Foundation/valuetransformer/transformedvalueclass%28%29.md) to return that type. Doing so populates [`allowedTopLevelClasses`](../Foundation/nssecureunarchivefromdatatransformer/allowedtoplevelclasses.md) automatically.
- If you expect to decode a top-level value of one of several allowed types, override [`allowedTopLevelClasses`](../Foundation/nssecureunarchivefromdatatransformer/allowedtoplevelclasses.md) to return those types.

The older [`unarchiveFromDataTransformerName`](../Foundation/nsvaluetransformername/unarchivefromdatatransformername.md) and [`keyedUnarchiveFromDataTransformerName`](../Foundation/nsvaluetransformername/keyedunarchivefromdatatransformername.md) values are now deprecated.

##### NSSecureCoding Conformance

The [`NSPointerFunctions`](../Foundation/nspointerfunctions.md), [`NSMapTable`](../Foundation/nsmaptable.md), and [`NSHashTable`](../Foundation/nshashtable.md) classes now support limited conformance to the [`NSSecureCoding`](../Foundation/nssecurecoding.md) protocol. You can securely encode pointer-function consuming collections as long as you configure them with the following personalities and kinds of memory:

- [`objectPersonality`](../Foundation/nspointerfunctions/options/objectpersonality.md)
- [`objectPointerPersonality`](../Foundation/nspointerfunctions/options/objectpointerpersonality.md)
- [`strongMemory`](../Foundation/nspointerfunctions/options/strongmemory.md)
- [`weakMemory`](../Foundation/nspointerfunctions/options/weakmemory.md)
- [`copyIn`](../Foundation/nspointerfunctions/options/copyin.md) (optional)

> ❗ **Important**: Weak values won’t round-trip as expected unless you strongly reference them elsewhere during unarchival.

##### Macro for Closed Enumerations

`NS_CLOSED_ENUM` is a new macro for declaring enumerations. You use it only for enumerations that are guaranteed to never gain an additional case. Usually you determine that there won’t be new cases because the enumeration you’re modeling represents a mathematically complete set. [`ComparisonResult`](../Foundation/comparisonresult.md) now adopts the `NS_CLOSED_ENUM` macro. It won’t ever gain additional cases.

> ❗ **Important**: Once an enumeration is marked as closed, it’s a binary- and source-incompatible change to add a new value. If you have any doubt about an enumeration gaining a private or additional public case in the future, use the `NS_ENUM` macro instead.

For information about `NS_CLOSED_ENUM` and choosing between it and other macros for grouping constants, see [Grouping Related Objective-C Constants](../Swift/grouping-related-objective-c-constants.md).

##### UserDefaults

[`UserDefaults`](../Foundation/userdefaults.md) has several bug fixes and improvements:

- Removed synchronization requirements. It’s no longer necessary to use [`synchronize()`](../Foundation/userdefaults/synchronize%28%29.md), [`CFPreferencesAppSynchronize(_:)`](../CoreFoundation/cfpreferencesappsynchronize%28_%29.md), or [`CFPreferencesSynchronize(_:_:_:)`](../CoreFoundation/cfpreferencessynchronize%28_,_,_%29.md). These methods will be deprecated in a future version of the OS.Now that you don’t need to call these synchronization methods, the performance characteristics of [`UserDefaults`](../Foundation/userdefaults.md) and Preferences Utilities are slightly different: The time taken for enqueueing write operations is now paid by the writing thread, rather than by the next thread to call [`synchronize()`](../Foundation/userdefaults/synchronize%28%29.md) or do a read operation.
- Removed retains when adding an observer. Adding observers to an instance of [`UserDefaults`](../Foundation/userdefaults.md) using the [`addObserver(_:forKeyPath:options:context:)`](../ObjectiveC/nsobject-swift.class/addobserver%28_,forkeypath,options,context%29.md) method unintentionally retained it, unlike all other uses of key-value observing. This has been corrected, and normal Cocoa memory management rules are now followed.
- Fixed key-value observing bug in [`UserDefaults`](../Foundation/userdefaults.md). Reading defaults on one thread while another thread set defaults could nondeterministically send key-value observing notifications on both threads, rather than just the thread doing the set operation. This is now fixed.

##### On-Demand Resources

[`NSBundleResourceRequest`](../Foundation/nsbundleresourcerequest.md) no longer throws exceptions when encountering certain kinds of internal errors. Instead, it returns an error in the error argument of the completion handler of the [`beginAccessingResources(completionHandler:)`](../Foundation/nsbundleresourcerequest/beginaccessingresources%28completionhandler%29.md) method. The error might include the [`NSFileReadUnknownError`](../Foundation/nsfilereadunknownerror-swift.var.md) and `NSXPCConnectionInterrupted` errors in addition to [`NSUserCancelledError`](../Foundation/nsusercancellederror-swift.var.md) and network-related errors.

If your app encounters an error when using [`NSBundleResourceRequest`](../Foundation/nsbundleresourcerequest.md), request the resource again or display a prompt to your user to try again.

##### Thread Safety of Bundles

The [`principalClass`](../Foundation/bundle/principalclass.md) property on [`Bundle`](../Foundation/bundle.md) includes new thread-safety improvements. Accessing the property blocks if other threads are in the process of loading the bundle. This action allows the property to return the correct value in all cases.

##### CFMessagePort

The [`CFMessagePortSetName(_:_:)`](../CoreFoundation/cfmessageportsetname%28_,_%29.md) function doesn’t do anything in apps linked on or after macOS 10.14, iOS 12, watchOS 5, and tvOS 12. This API will be deprecated in a future release.

In apps linked on earlier versions of macOS, iOS, watchOS, and tvOS, the [`CFMessagePortSetName(_:_:)`](../CoreFoundation/cfmessageportsetname%28_,_%29.md) function doesn’t do anything if the message port already has a dispatch queue associated with itself via the [`CFMessagePortSetDispatchQueue(_:_:)`](../CoreFoundation/cfmessageportsetdispatchqueue%28_,_%29.md) function. Previously, this pattern would result in undefined behavior.

In all cases, if you need to change the name of a [`CFMessagePort`](../CoreFoundation/cfmessageport.md), use [`CFMessagePortCreateLocal(_:_:_:_:_:)`](../CoreFoundation/cfmessageportcreatelocal%28_,_,_,_,_%29.md) or [`CFMessagePortCreateRemote(_:_:)`](../CoreFoundation/cfmessageportcreateremote%28_,_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/foundation-release-notes)*