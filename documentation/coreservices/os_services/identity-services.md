# Identity Services

**Framework**: Core Services

Access the system's user and group database and manage access controls.

#### Overview

The Core Services Identity Reference allows developers to support user and group creation, enumeration, attribute inspection, credential management as well as group membership management in their applications.

## Topics

### Classes
- [class CSIdentity](csidentity.md)
- [class CSIdentityAuthority](csidentityauthority.md)
- [class CSIdentityQuery](csidentityquery.md)
### Functions
- [func CSDiskSpaceCancelRecovery(CFUUID!)](1448335-csdiskspacecancelrecovery.md)
- [func CSDiskSpaceGetRecoveryEstimate(CFURL!) -> UInt64](1448439-csdiskspacegetrecoveryestimate.md)
- [func CSDiskSpaceStartRecovery(CFURL!, UInt64, CSDiskSpaceRecoveryOptions, UnsafeMutablePointer<Unmanaged<CFUUID>?>!, dispatch_queue_t!, CSDiskSpaceRecoveryCallback!)](1447968-csdiskspacestartrecovery.md)
- [func CSGetDefaultIdentityAuthority() -> Unmanaged<CSIdentityAuthority>!](1448826-csgetdefaultidentityauthority.md)
- [func CSGetLocalIdentityAuthority() -> Unmanaged<CSIdentityAuthority>!](1444814-csgetlocalidentityauthority.md)
- [func CSGetManagedIdentityAuthority() -> Unmanaged<CSIdentityAuthority>!](1446750-csgetmanagedidentityauthority.md)
- [func CSIdentityAddAlias(CSIdentity!, CFString!)](1443062-csidentityaddalias.md)
- [func CSIdentityAddMember(CSIdentity!, CSIdentity!)](1447513-csidentityaddmember.md)
- [func CSIdentityAuthenticateUsingPassword(CSIdentity!, CFString!) -> Bool](1449855-csidentityauthenticateusingpassw.md)
- [func CSIdentityAuthorityCopyLocalizedName(CSIdentityAuthority!) -> Unmanaged<CFString>!](1448990-csidentityauthoritycopylocalized.md)
- [func CSIdentityAuthorityGetTypeID() -> CFTypeID](1449199-csidentityauthoritygettypeid.md)
- [func CSIdentityCommit(CSIdentity!, AuthorizationRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](1449575-csidentitycommit.md)
- [func CSIdentityCommitAsynchronously(CSIdentity!, UnsafePointer<CSIdentityClientContext>!, CFRunLoop!, CFString!, AuthorizationRef!) -> Bool](1447936-csidentitycommitasynchronously.md)
- [func CSIdentityCreate(CFAllocator!, CSIdentityClass, CFString!, CFString!, CSIdentityFlags, CSIdentityAuthority!) -> Unmanaged<CSIdentity>!](1447616-csidentitycreate.md)
- [func CSIdentityCreateCopy(CFAllocator!, CSIdentity!) -> Unmanaged<CSIdentity>!](1443553-csidentitycreatecopy.md)
- [func CSIdentityCreateGroupMembershipQuery(CFAllocator!, CSIdentity!) -> Unmanaged<CSIdentityQuery>!](1448605-csidentitycreategroupmembershipq.md)
- [func CSIdentityCreatePersistentReference(CFAllocator!, CSIdentity!) -> Unmanaged<CFData>!](1444037-csidentitycreatepersistentrefere.md)
- [func CSIdentityDelete(CSIdentity!)](1442616-csidentitydelete.md)
- [func CSIdentityGetAliases(CSIdentity!) -> Unmanaged<CFArray>!](1446455-csidentitygetaliases.md)
- [func CSIdentityGetAuthority(CSIdentity!) -> Unmanaged<CSIdentityAuthority>!](1446828-csidentitygetauthority.md)
- [func CSIdentityGetCertificate(CSIdentity!) -> Unmanaged<SecCertificate>!](1448582-csidentitygetcertificate.md)
- [func CSIdentityGetClass(CSIdentity!) -> CSIdentityClass](1447194-csidentitygetclass.md)
- [func CSIdentityGetEmailAddress(CSIdentity!) -> Unmanaged<CFString>!](1446211-csidentitygetemailaddress.md)
- [func CSIdentityGetFullName(CSIdentity!) -> Unmanaged<CFString>!](1447315-csidentitygetfullname.md)
- [func CSIdentityGetImageData(CSIdentity!) -> Unmanaged<CFData>!](1444544-csidentitygetimagedata.md)
- [func CSIdentityGetImageDataType(CSIdentity!) -> Unmanaged<CFString>!](1447478-csidentitygetimagedatatype.md)
- [func CSIdentityGetImageURL(CSIdentity!) -> Unmanaged<CFURL>!](1446099-csidentitygetimageurl.md)
- [func CSIdentityGetPosixID(CSIdentity!) -> id_t](1443230-csidentitygetposixid.md)
- [func CSIdentityGetPosixName(CSIdentity!) -> Unmanaged<CFString>!](1447210-csidentitygetposixname.md)
- [func CSIdentityGetTypeID() -> CFTypeID](1444732-csidentitygettypeid.md)
- [func CSIdentityGetUUID(CSIdentity!) -> Unmanaged<CFUUID>!](1447987-csidentitygetuuid.md)
- [func CSIdentityIsCommitting(CSIdentity!) -> Bool](1449734-csidentityiscommitting.md)
- [func CSIdentityIsEnabled(CSIdentity!) -> Bool](1443379-csidentityisenabled.md)
- [func CSIdentityIsHidden(CSIdentity!) -> Bool](1449476-csidentityishidden.md)
- [func CSIdentityIsMemberOfGroup(CSIdentity!, CSIdentity!) -> Bool](1449237-csidentityismemberofgroup.md)
- [func CSIdentityQueryCopyResults(CSIdentityQuery!) -> Unmanaged<CFArray>!](1429035-csidentityquerycopyresults.md)
- [func CSIdentityQueryCreate(CFAllocator!, CSIdentityClass, CSIdentityAuthority!) -> Unmanaged<CSIdentityQuery>!](1429003-csidentityquerycreate.md)
- [func CSIdentityQueryCreateForCurrentUser(CFAllocator!) -> Unmanaged<CSIdentityQuery>!](1429037-csidentityquerycreateforcurrentu.md)
- [func CSIdentityQueryCreateForName(CFAllocator!, CFString!, CSIdentityQueryStringComparisonMethod, CSIdentityClass, CSIdentityAuthority!) -> Unmanaged<CSIdentityQuery>!](1428997-csidentityquerycreateforname.md)
- [func CSIdentityQueryCreateForPersistentReference(CFAllocator!, CFData!) -> Unmanaged<CSIdentityQuery>!](1428991-csidentityquerycreateforpersiste.md)
- [func CSIdentityQueryCreateForPosixID(CFAllocator!, id_t, CSIdentityClass, CSIdentityAuthority!) -> Unmanaged<CSIdentityQuery>!](1428990-csidentityquerycreateforposixid.md)
- [func CSIdentityQueryCreateForUUID(CFAllocator!, CFUUID!, CSIdentityAuthority!) -> Unmanaged<CSIdentityQuery>!](1429007-csidentityquerycreateforuuid.md)
- [func CSIdentityQueryExecute(CSIdentityQuery!, CSIdentityQueryFlags, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](1429041-csidentityqueryexecute.md)
- [func CSIdentityQueryExecuteAsynchronously(CSIdentityQuery!, CSIdentityQueryFlags, UnsafePointer<CSIdentityQueryClientContext>!, CFRunLoop!, CFString!) -> Bool](1429011-csidentityqueryexecuteasynchrono.md)
- [func CSIdentityQueryGetTypeID() -> CFTypeID](1429012-csidentityquerygettypeid.md)
- [func CSIdentityQueryStop(CSIdentityQuery!)](1429047-csidentityquerystop.md)
- [func CSIdentityRemoveAlias(CSIdentity!, CFString!)](1442114-csidentityremovealias.md)
- [func CSIdentityRemoveClient(CSIdentity!)](1448933-csidentityremoveclient.md)
- [func CSIdentityRemoveMember(CSIdentity!, CSIdentity!)](1448796-csidentityremovemember.md)
- [func CSIdentitySetCertificate(CSIdentity!, SecCertificate!)](1447691-csidentitysetcertificate.md)
- [func CSIdentitySetEmailAddress(CSIdentity!, CFString!)](1443235-csidentitysetemailaddress.md)
- [func CSIdentitySetFullName(CSIdentity!, CFString!)](1446623-csidentitysetfullname.md)
- [func CSIdentitySetImageData(CSIdentity!, CFData!, CFString!)](1441866-csidentitysetimagedata.md)
- [func CSIdentitySetImageURL(CSIdentity!, CFURL!)](1446717-csidentitysetimageurl.md)
- [func CSIdentitySetIsEnabled(CSIdentity!, Bool)](1443028-csidentitysetisenabled.md)
- [func CSIdentitySetPassword(CSIdentity!, CFString!)](1443568-csidentitysetpassword.md)
### Structures
- [struct CSIdentityClientContext](csidentityclientcontext.md)
- [struct CSIdentityQueryClientContext](csidentityqueryclientcontext.md)
### Constants
- [let kCSIdentityErrorDomain: CFString!](kcsidentityerrordomain.md)
- [let kCSIdentityGeneratePosixName: CFString!](kcsidentitygenerateposixname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/os_services/identity_services)*