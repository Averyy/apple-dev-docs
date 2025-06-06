# dnssd

**Framework**: dnssd  
**Kind**: module

Discover, publish, and resolve network services on a local area or wide area network.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

#### Overview

The DNS Service Discovery API helps you to perform three main tasks:

- Registering a service.
- Browsing for services.
- Resolving service names to host names.

In support of these main tasks, this API can directly assist you in performing two subsidiary tasks:

- Enumerating domains (finding recommended service domains).
- Updating registrations (changing your DNS registration data dynamically).

Most apps shouldn’t use this API, and instead should use a higher-level service discovery API like [`NetService`](https://developer.apple.com/documentation/Foundation/NetService). Use dnssd if you’re writing BSD-style applications or cross-platform programs that don’t need to link to higher-level frameworks. You can also use dnssd if you need specific lower-level functionality exposed by this API.

> ❗ **Important**:  Apps that use the local network must provide a usage string in their `Info.plist` file with the key [`NSLocalNetworkUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription). Apps that use [`Bonjour`](https://developer.apple.com/documentation/Foundation/bonjour) must also declare the services they browse, using the [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) key.

 Apps that use the local network must provide a usage string in their `Info.plist` file with the key [`NSLocalNetworkUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription). Apps that use [`Bonjour`](https://developer.apple.com/documentation/Foundation/bonjour) must also declare the services they browse, using the [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) key.

## Topics

### Reference
- [DNS Service Discovery C](dns-service-discovery-c.md)
  See the Overview section above for header-level documentation.
- [dnssd Enumerations](dnssd-enumerations.md)
- [dnssd Functions](dnssd-functions.md)
- [dnssd Data Types](dnssd-data-types.md)
- [dnssd Constants](dnssd-constants.md)
### Variables
- [var kDNSServiceAAAAPolicyFallback: DNSServiceAAAAPolicy](kdnsserviceaaaapolicyfallback.md)
- [var kDNSServiceAAAAPolicyNone: DNSServiceAAAAPolicy](kdnsserviceaaaapolicynone.md)
- [var kDNSServiceClass_IN: Int](kdnsserviceclass_in.md)
- [var kDNSServiceErr_AlreadyRegistered: Int](kdnsserviceerr_alreadyregistered.md)
- [var kDNSServiceErr_BadFlags: Int](kdnsserviceerr_badflags.md)
- [var kDNSServiceErr_BadInterfaceIndex: Int](kdnsserviceerr_badinterfaceindex.md)
- [var kDNSServiceErr_BadKey: Int](kdnsserviceerr_badkey.md)
- [var kDNSServiceErr_BadParam: Int](kdnsserviceerr_badparam.md)
- [var kDNSServiceErr_BadReference: Int](kdnsserviceerr_badreference.md)
- [var kDNSServiceErr_BadSig: Int](kdnsserviceerr_badsig.md)
- [var kDNSServiceErr_BadState: Int](kdnsserviceerr_badstate.md)
- [var kDNSServiceErr_BadTime: Int](kdnsserviceerr_badtime.md)
- [var kDNSServiceErr_DefunctConnection: Int](kdnsserviceerr_defunctconnection.md)
- [var kDNSServiceErr_DoubleNAT: Int](kdnsserviceerr_doublenat.md)
- [var kDNSServiceErr_Firewall: Int](kdnsserviceerr_firewall.md)
- [var kDNSServiceErr_Incompatible: Int](kdnsserviceerr_incompatible.md)
- [var kDNSServiceErr_Invalid: Int](kdnsserviceerr_invalid.md)
- [var kDNSServiceErr_NATPortMappingDisabled: Int](kdnsserviceerr_natportmappingdisabled.md)
- [var kDNSServiceErr_NATPortMappingUnsupported: Int](kdnsserviceerr_natportmappingunsupported.md)
- [var kDNSServiceErr_NATTraversal: Int](kdnsserviceerr_nattraversal.md)
- [var kDNSServiceErr_NameConflict: Int](kdnsserviceerr_nameconflict.md)
- [var kDNSServiceErr_NoAuth: Int](kdnsserviceerr_noauth.md)
- [var kDNSServiceErr_NoError: Int](kdnsserviceerr_noerror.md)
- [var kDNSServiceErr_NoMemory: Int](kdnsserviceerr_nomemory.md)
- [var kDNSServiceErr_NoRouter: Int](kdnsserviceerr_norouter.md)
- [var kDNSServiceErr_NoSuchKey: Int](kdnsserviceerr_nosuchkey.md)
- [var kDNSServiceErr_NoSuchName: Int](kdnsserviceerr_nosuchname.md)
- [var kDNSServiceErr_NoSuchRecord: Int](kdnsserviceerr_nosuchrecord.md)
- [var kDNSServiceErr_NotInitialized: Int](kdnsserviceerr_notinitialized.md)
- [var kDNSServiceErr_NotPermitted: Int](kdnsserviceerr_notpermitted.md)
- [var kDNSServiceErr_PolicyDenied: Int](kdnsserviceerr_policydenied.md)
- [var kDNSServiceErr_PollingMode: Int](kdnsserviceerr_pollingmode.md)
- [var kDNSServiceErr_Refused: Int](kdnsserviceerr_refused.md)
- [var kDNSServiceErr_ServiceNotRunning: Int](kdnsserviceerr_servicenotrunning.md)
- [var kDNSServiceErr_StaleData: Int](kdnsserviceerr_staledata.md)
- [var kDNSServiceErr_Timeout: Int](kdnsserviceerr_timeout.md)
- [var kDNSServiceErr_Transient: Int](kdnsserviceerr_transient.md)
- [var kDNSServiceErr_Unknown: Int](kdnsserviceerr_unknown.md)
- [var kDNSServiceErr_Unsupported: Int](kdnsserviceerr_unsupported.md)
- [var kDNSServiceFlagAnsweredFromCache: UInt32](kdnsserviceflagansweredfromcache.md)
- [var kDNSServiceFlagsAdd: UInt32](kdnsserviceflagsadd.md)
- [var kDNSServiceFlagsAllowExpiredAnswers: UInt32](kdnsserviceflagsallowexpiredanswers.md)
- [var kDNSServiceFlagsAllowRemoteQuery: UInt32](kdnsserviceflagsallowremotequery.md)
- [var kDNSServiceFlagsAutoTrigger: UInt32](kdnsserviceflagsautotrigger.md)
- [var kDNSServiceFlagsBackgroundTrafficClass: UInt32](kdnsserviceflagsbackgroundtrafficclass.md)
- [var kDNSServiceFlagsBogus: UInt32](kdnsserviceflagsbogus.md)
- [var kDNSServiceFlagsBrowseDomains: UInt32](kdnsserviceflagsbrowsedomains.md)
- [var kDNSServiceFlagsDefault: UInt32](kdnsserviceflagsdefault.md)
- [var kDNSServiceFlagsEnableDNSSEC: UInt32](kdnsserviceflagsenablednssec.md)
- [var kDNSServiceFlagsExpiredAnswer: UInt32](kdnsserviceflagsexpiredanswer.md)
- [var kDNSServiceFlagsForce: UInt32](kdnsserviceflagsforce.md)
- [var kDNSServiceFlagsForceMulticast: UInt32](kdnsserviceflagsforcemulticast.md)
- [var kDNSServiceFlagsIncludeAWDL: UInt32](kdnsserviceflagsincludeawdl.md)
- [var kDNSServiceFlagsIncludeP2P: UInt32](kdnsserviceflagsincludep2p.md)
- [var kDNSServiceFlagsIndeterminate: UInt32](kdnsserviceflagsindeterminate.md)
- [var kDNSServiceFlagsInsecure: UInt32](kdnsserviceflagsinsecure.md)
- [var kDNSServiceFlagsKnownUnique: UInt32](kdnsserviceflagsknownunique.md)
- [var kDNSServiceFlagsLongLivedQuery: UInt32](kdnsserviceflagslonglivedquery.md)
- [var kDNSServiceFlagsMoreComing: UInt32](kdnsserviceflagsmorecoming.md)
- [var kDNSServiceFlagsNoAutoRename: UInt32](kdnsserviceflagsnoautorename.md)
- [var kDNSServiceFlagsPrivateFive: UInt32](kdnsserviceflagsprivatefive.md)
- [var kDNSServiceFlagsPrivateFour: UInt32](kdnsserviceflagsprivatefour.md)
- [var kDNSServiceFlagsPrivateOne: UInt32](kdnsserviceflagsprivateone.md)
- [var kDNSServiceFlagsPrivateThree: UInt32](kdnsserviceflagsprivatethree.md)
- [var kDNSServiceFlagsPrivateTwo: UInt32](kdnsserviceflagsprivatetwo.md)
- [var kDNSServiceFlagsQueueRequest: UInt32](kdnsserviceflagsqueuerequest.md)
- [var kDNSServiceFlagsRegistrationDomains: UInt32](kdnsserviceflagsregistrationdomains.md)
- [var kDNSServiceFlagsReturnIntermediates: UInt32](kdnsserviceflagsreturnintermediates.md)
- [var kDNSServiceFlagsSecure: UInt32](kdnsserviceflagssecure.md)
- [var kDNSServiceFlagsShareConnection: UInt32](kdnsserviceflagsshareconnection.md)
- [var kDNSServiceFlagsShared: UInt32](kdnsserviceflagsshared.md)
- [var kDNSServiceFlagsSuppressUnusable: UInt32](kdnsserviceflagssuppressunusable.md)
- [var kDNSServiceFlagsThresholdFinder: UInt32](kdnsserviceflagsthresholdfinder.md)
- [var kDNSServiceFlagsThresholdOne: UInt32](kdnsserviceflagsthresholdone.md)
- [var kDNSServiceFlagsThresholdReached: UInt32](kdnsserviceflagsthresholdreached.md)
- [var kDNSServiceFlagsTimeout: UInt32](kdnsserviceflagstimeout.md)
- [var kDNSServiceFlagsUnicastResponse: UInt32](kdnsserviceflagsunicastresponse.md)
- [var kDNSServiceFlagsUnique: UInt32](kdnsserviceflagsunique.md)
- [var kDNSServiceFlagsValidate: UInt32](kdnsserviceflagsvalidate.md)
- [var kDNSServiceFlagsValidateOptional: UInt32](kdnsserviceflagsvalidateoptional.md)
- [var kDNSServiceFlagsWakeOnResolve: UInt32](kdnsserviceflagswakeonresolve.md)
- [var kDNSServiceFlagsWakeOnlyService: UInt32](kdnsserviceflagswakeonlyservice.md)
- [var kDNSServiceProtocol_IPv4: Int](kdnsserviceprotocol_ipv4.md)
- [var kDNSServiceProtocol_IPv6: Int](kdnsserviceprotocol_ipv6.md)
- [var kDNSServiceProtocol_TCP: Int](kdnsserviceprotocol_tcp.md)
- [var kDNSServiceProtocol_UDP: Int](kdnsserviceprotocol_udp.md)
- [var kDNSServiceType_A: Int](kdnsservicetype_a.md)
- [var kDNSServiceType_A6: Int](kdnsservicetype_a6.md)
- [var kDNSServiceType_AAAA: Int](kdnsservicetype_aaaa.md)
- [var kDNSServiceType_AFSDB: Int](kdnsservicetype_afsdb.md)
- [var kDNSServiceType_ANY: Int](kdnsservicetype_any.md)
- [var kDNSServiceType_APL: Int](kdnsservicetype_apl.md)
- [var kDNSServiceType_ATMA: Int](kdnsservicetype_atma.md)
- [var kDNSServiceType_AXFR: Int](kdnsservicetype_axfr.md)
- [var kDNSServiceType_CERT: Int](kdnsservicetype_cert.md)
- [var kDNSServiceType_CNAME: Int](kdnsservicetype_cname.md)
- [var kDNSServiceType_DHCID: Int](kdnsservicetype_dhcid.md)
- [var kDNSServiceType_DNAME: Int](kdnsservicetype_dname.md)
- [var kDNSServiceType_DNSKEY: Int](kdnsservicetype_dnskey.md)
- [var kDNSServiceType_DS: Int](kdnsservicetype_ds.md)
- [var kDNSServiceType_EID: Int](kdnsservicetype_eid.md)
- [var kDNSServiceType_GID: Int](kdnsservicetype_gid.md)
- [var kDNSServiceType_GPOS: Int](kdnsservicetype_gpos.md)
- [var kDNSServiceType_HINFO: Int](kdnsservicetype_hinfo.md)
- [var kDNSServiceType_HIP: Int](kdnsservicetype_hip.md)
- [var kDNSServiceType_HTTPS: Int](kdnsservicetype_https.md)
- [var kDNSServiceType_IPSECKEY: Int](kdnsservicetype_ipseckey.md)
- [var kDNSServiceType_ISDN: Int](kdnsservicetype_isdn.md)
- [var kDNSServiceType_IXFR: Int](kdnsservicetype_ixfr.md)
- [var kDNSServiceType_KEY: Int](kdnsservicetype_key.md)
- [var kDNSServiceType_KX: Int](kdnsservicetype_kx.md)
- [var kDNSServiceType_LOC: Int](kdnsservicetype_loc.md)
- [var kDNSServiceType_MAILA: Int](kdnsservicetype_maila.md)
- [var kDNSServiceType_MAILB: Int](kdnsservicetype_mailb.md)
- [var kDNSServiceType_MB: Int](kdnsservicetype_mb.md)
- [var kDNSServiceType_MD: Int](kdnsservicetype_md.md)
- [var kDNSServiceType_MF: Int](kdnsservicetype_mf.md)
- [var kDNSServiceType_MG: Int](kdnsservicetype_mg.md)
- [var kDNSServiceType_MINFO: Int](kdnsservicetype_minfo.md)
- [var kDNSServiceType_MR: Int](kdnsservicetype_mr.md)
- [var kDNSServiceType_MX: Int](kdnsservicetype_mx.md)
- [var kDNSServiceType_NAPTR: Int](kdnsservicetype_naptr.md)
- [var kDNSServiceType_NIMLOC: Int](kdnsservicetype_nimloc.md)
- [var kDNSServiceType_NS: Int](kdnsservicetype_ns.md)
- [var kDNSServiceType_NSAP: Int](kdnsservicetype_nsap.md)
- [var kDNSServiceType_NSAP_PTR: Int](kdnsservicetype_nsap_ptr.md)
- [var kDNSServiceType_NSEC: Int](kdnsservicetype_nsec.md)
- [var kDNSServiceType_NSEC3: Int](kdnsservicetype_nsec3.md)
- [var kDNSServiceType_NSEC3PARAM: Int](kdnsservicetype_nsec3param.md)
- [var kDNSServiceType_NULL: Int](kdnsservicetype_null.md)
- [var kDNSServiceType_NXT: Int](kdnsservicetype_nxt.md)
- [var kDNSServiceType_OPT: Int](kdnsservicetype_opt.md)
- [var kDNSServiceType_PTR: Int](kdnsservicetype_ptr.md)
- [var kDNSServiceType_PX: Int](kdnsservicetype_px.md)
- [var kDNSServiceType_RP: Int](kdnsservicetype_rp.md)
- [var kDNSServiceType_RRSIG: Int](kdnsservicetype_rrsig.md)
- [var kDNSServiceType_RT: Int](kdnsservicetype_rt.md)
- [var kDNSServiceType_SIG: Int](kdnsservicetype_sig.md)
- [var kDNSServiceType_SINK: Int](kdnsservicetype_sink.md)
- [var kDNSServiceType_SOA: Int](kdnsservicetype_soa.md)
- [var kDNSServiceType_SPF: Int](kdnsservicetype_spf.md)
- [var kDNSServiceType_SRV: Int](kdnsservicetype_srv.md)
- [var kDNSServiceType_SSHFP: Int](kdnsservicetype_sshfp.md)
- [var kDNSServiceType_SVCB: Int](kdnsservicetype_svcb.md)
- [var kDNSServiceType_TKEY: Int](kdnsservicetype_tkey.md)
- [var kDNSServiceType_TSIG: Int](kdnsservicetype_tsig.md)
- [var kDNSServiceType_TXT: Int](kdnsservicetype_txt.md)
- [var kDNSServiceType_UID: Int](kdnsservicetype_uid.md)
- [var kDNSServiceType_UINFO: Int](kdnsservicetype_uinfo.md)
- [var kDNSServiceType_UNSPEC: Int](kdnsservicetype_unspec.md)
- [var kDNSServiceType_WKS: Int](kdnsservicetype_wks.md)
- [var kDNSServiceType_X25: Int](kdnsservicetype_x25.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd)*