# init(keyExchangeKeys:dbSignatures:dbxSignatures:)

**Framework**: Virtualization  
**Kind**: init

Creates a signature lists container from signature list objects.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init(keyExchangeKeys: [VZEFISignatureList], dbSignatures: [VZEFISignatureList], dbxSignatures: [VZEFISignatureList])
```

#### Discussion

> ⚠️ **Warning**: Make sure that the signature data is in the correct format. Applying a malformed configuration may corrupt the variable store and render the guest unbootable.

This initializer creates a container holding signature lists for all three UEFI Secure Boot databases.

The following example demonstrates the creation of a `VZEFISignatureDatabaseConfiguration` with a fully custom configuration.

**Swift**:

```swift
 do {
     // Load platform key certificate.
     let platformKeyData = try Data(contentsOf: URL(fileURLWithPath: "/path/to/PK.der"))
     guard let platformKey = SecCertificateCreateWithData(nil, platformKeyData as CFData) else {
         // Handle error.
     }

     // Create signature lists from files.
     let kekList = try VZEFISignatureList(contentsOf: URL(fileURLWithPath: "/path/to/KEK.bin"))
     let dbList = try VZEFISignatureList(contentsOf: URL(fileURLWithPath: "/path/to/db.bin"))
     let dbxList = try VZEFISignatureList(contentsOf: URL(fileURLWithPath: "/path/to/dbx.sha256"))
     let signatures = VZEFISignatureDatabaseConfiguration(
         keyExchangeKeys: [kekList],
         dbSignatures: [dbList],
         dbxSignatures: [dbxList]
     )

     // Enable Secure Boot with custom Platform Key.
     try variableStore.enableSecureBoot(platformKey: platformKey)

     // Enroll custom signatures.
     try variableStore.enrollSecureBootSignatures(signatures)
 } catch {
     // Handle error.
 }
```

**Objective-C**:

```objc
 // Load Platform Key certificate.
 NSData *platformKeyData = [NSData dataWithContentsOfURL:[NSURL fileURLWithPath:@"/path/to/PK.der"]];
 SecCertificateRef platformKey = SecCertificateCreateWithData(NULL, (__bridge CFDataRef)platformKeyData);
 if (!platformKey) {
     // Handle error.
 }

 // Create signature lists from files.
 NSError *error;
 VZEFISignatureList *kekList = [[VZEFISignatureList alloc] initWithContentsOfURL:[NSURL fileURLWithPath:@"/path/to/KEK.bin"] error:&error];
 VZEFISignatureList *dbList = [[VZEFISignatureList alloc] initWithContentsOfURL:[NSURL fileURLWithPath:@"/path/to/db.bin"] error:&error];
 VZEFISignatureList *dbxList = [[VZEFISignatureList alloc] initWithContentsOfURL:[NSURL fileURLWithPath:@"/path/to/dbx.sha256"] error:&error];
 if (!kekList || !dbList || !dbxList) {
     // Handle error.
 }
 VZEFISignatureDatabaseConfiguration *signatures = [[VZEFISignatureDatabaseConfiguration alloc] initWithKeyExchangeKeys:@[ kekList ]
                                        dbSignatures:@[ dbList ]
                                        dbxSignatures:@[ dbxList ]];

 // Enable secure boot with custom Platform Key.
 if (![variableStore enableSecureBootWithPlatformKey:platformKey error:&error]) {
     // Handle error.
 }

 // Enroll custom signatures.
 if (![variableStore enrollSecureBootSignatures:signatures error:&error]) {
     // Handle error.
 }

 CFRelease(platformKey);
```

## Parameters

- `keyExchangeKeys`: An array of [`VZEFISignatureList`](vzefisignaturelist.md) objects for the Key Exchange Key (KEK) database. Must contain only X.509 certificates. If any signature list contains SHA-256 hashes, the framework raises an exception. This parameter can be empty if you don’t need to add KEK signatures.
- `dbSignatures`: An array of [`VZEFISignatureList`](vzefisignaturelist.md) objects for the allowed signature database (db). This parameter can be empty if you don’t need to add allowed signatures.
- `dbxSignatures`: An array of [`VZEFISignatureList`](vzefisignaturelist.md) objects for the forbidden signature database (dbx). This parameter can be empty if you don’t need to add forbidden signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefisignaturedatabaseconfiguration/init(keyexchangekeys:dbsignatures:dbxsignatures:))*