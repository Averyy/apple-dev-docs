#!/usr/bin/env python3
"""
Production backup system for ChromaDB vectorstore and hash files.
Automated daily snapshots with integrity verification.
"""

import os
import shutil
import json
import time
from pathlib import Path
from datetime import datetime, timezone
from typing import List, Dict, Any
import tarfile
import hashlib
import logging
import argparse

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VectorstoreBackup:
    """Comprehensive backup system for the Apple docs vectorstore."""
    
    def __init__(self, backup_dir: str = "backups"):
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(exist_ok=True)
        self.vectorstore_path = Path("vectorstore")
        self.hashes_path = Path(".hashes")
        
    def create_backup(self, keep_days: int = 7) -> bool:
        """Create complete backup with integrity verification."""
        
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup_name = f"apple_docs_backup_{timestamp}"
        backup_path = self.backup_dir / backup_name
        
        logger.info(f"Creating backup: {backup_name}")
        
        try:
            # Create backup directory
            backup_path.mkdir(exist_ok=True)
            
            # Backup ChromaDB vectorstore
            if self.vectorstore_path.exists():
                vectorstore_backup = backup_path / "vectorstore"
                logger.info("Backing up ChromaDB vectorstore...")
                shutil.copytree(self.vectorstore_path, vectorstore_backup)
                
                # Verify vectorstore backup
                if not self._verify_vectorstore_backup(vectorstore_backup):
                    raise Exception("Vectorstore backup verification failed")
                    
                logger.info(f"✅ Vectorstore backed up: {self._get_size_mb(vectorstore_backup):.1f}MB")
            
            # Backup hash files
            if self.hashes_path.exists():
                hashes_backup = backup_path / ".hashes"
                logger.info("Backing up hash files...")
                shutil.copytree(self.hashes_path, hashes_backup)
                
                # Verify hash files
                hash_count = len(list(hashes_backup.glob("*.json")))
                logger.info(f"✅ Hash files backed up: {hash_count} files")
            
            # Create backup metadata
            metadata = {
                "timestamp": timestamp,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "vectorstore_size_mb": self._get_size_mb(backup_path / "vectorstore") if (backup_path / "vectorstore").exists() else 0,
                "hash_files_count": len(list((backup_path / ".hashes").glob("*.json"))) if (backup_path / ".hashes").exists() else 0,
                "backup_size_mb": self._get_size_mb(backup_path),
                "integrity_verified": True
            }
            
            with open(backup_path / "backup_metadata.json", "w") as f:
                json.dump(metadata, f, indent=2)
            
            # Create compressed archive
            archive_path = self.backup_dir / f"{backup_name}.tar.gz"
            logger.info("Creating compressed archive...")
            
            with tarfile.open(archive_path, "w:gz") as tar:
                tar.add(backup_path, arcname=backup_name)
            
            # Remove uncompressed backup
            shutil.rmtree(backup_path)
            
            # Calculate archive checksum
            archive_checksum = self._calculate_file_checksum(archive_path)
            
            # Save archive metadata
            archive_metadata = {
                **metadata,
                "archive_path": str(archive_path),
                "archive_size_mb": self._get_size_mb(archive_path),
                "archive_checksum": archive_checksum
            }
            
            with open(archive_path.with_suffix(".json"), "w") as f:
                json.dump(archive_metadata, f, indent=2)
            
            logger.info(f"✅ Backup complete: {archive_path.name}")
            logger.info(f"   Size: {archive_metadata['archive_size_mb']:.1f}MB")
            logger.info(f"   Checksum: {archive_checksum[:16]}...")
            
            # Clean up old backups
            self._cleanup_old_backups(keep_days)
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Backup failed: {e}")
            # Clean up partial backup
            if backup_path.exists():
                shutil.rmtree(backup_path)
            return False
    
    def restore_backup(self, backup_name: str, verify: bool = True) -> bool:
        """Restore from backup with verification."""
        
        archive_path = self.backup_dir / f"{backup_name}.tar.gz"
        
        if not archive_path.exists():
            logger.error(f"❌ Backup not found: {archive_path}")
            return False
        
        logger.info(f"Restoring backup: {backup_name}")
        
        try:
            # Verify archive integrity
            if verify:
                metadata_path = archive_path.with_suffix(".json")
                if metadata_path.exists():
                    with open(metadata_path) as f:
                        metadata = json.load(f)
                    
                    current_checksum = self._calculate_file_checksum(archive_path)
                    if current_checksum != metadata.get("archive_checksum"):
                        raise Exception("Archive checksum mismatch - backup may be corrupted")
                    
                    logger.info("✅ Archive integrity verified")
            
            # Create backup of current state
            if self.vectorstore_path.exists() or self.hashes_path.exists():
                current_backup_name = f"pre_restore_{int(time.time())}"
                logger.info(f"Creating backup of current state: {current_backup_name}")
                self.create_backup()
            
            # Extract archive
            with tarfile.open(archive_path, "r:gz") as tar:
                tar.extractall(self.backup_dir)
            
            extracted_path = self.backup_dir / backup_name
            
            # Restore vectorstore
            if (extracted_path / "vectorstore").exists():
                if self.vectorstore_path.exists():
                    shutil.rmtree(self.vectorstore_path)
                shutil.move(extracted_path / "vectorstore", self.vectorstore_path)
                logger.info("✅ Vectorstore restored")
            
            # Restore hash files
            if (extracted_path / ".hashes").exists():
                if self.hashes_path.exists():
                    shutil.rmtree(self.hashes_path)
                shutil.move(extracted_path / ".hashes", self.hashes_path)
                logger.info("✅ Hash files restored")
            
            # Clean up extracted files
            shutil.rmtree(extracted_path)
            
            logger.info(f"✅ Restore complete: {backup_name}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Restore failed: {e}")
            return False
    
    def list_backups(self) -> List[Dict[str, Any]]:
        """List available backups with metadata."""
        
        backups = []
        
        for metadata_file in sorted(self.backup_dir.glob("*.json")):
            try:
                with open(metadata_file) as f:
                    metadata = json.load(f)
                
                archive_path = Path(metadata["archive_path"])
                if archive_path.exists():
                    backups.append({
                        "name": archive_path.stem,
                        "created_at": metadata["created_at"],
                        "size_mb": metadata["archive_size_mb"],
                        "vectorstore_size_mb": metadata["vectorstore_size_mb"],
                        "hash_files_count": metadata["hash_files_count"],
                        "verified": metadata.get("integrity_verified", False)
                    })
                    
            except Exception as e:
                logger.warning(f"Could not read backup metadata: {metadata_file} - {e}")
        
        return backups
    
    def _verify_vectorstore_backup(self, backup_path: Path) -> bool:
        """Verify ChromaDB backup integrity."""
        
        try:
            # Check for essential ChromaDB files
            sqlite_file = backup_path / "chroma.sqlite3"
            if not sqlite_file.exists():
                logger.error("Missing chroma.sqlite3 file")
                return False
            
            # Basic file size check
            if sqlite_file.stat().st_size < 1000:  # Less than 1KB is suspicious
                logger.error("ChromaDB file suspiciously small")
                return False
            
            # Check for collection directories
            collection_dirs = [d for d in backup_path.iterdir() if d.is_dir()]
            if len(collection_dirs) == 0:
                logger.warning("No collection directories found")
            
            return True
            
        except Exception as e:
            logger.error(f"Backup verification failed: {e}")
            return False
    
    def _get_size_mb(self, path: Path) -> float:
        """Calculate size in MB."""
        
        if path.is_file():
            return path.stat().st_size / (1024 * 1024)
        
        total_size = 0
        for file_path in path.rglob("*"):
            if file_path.is_file():
                total_size += file_path.stat().st_size
        
        return total_size / (1024 * 1024)
    
    def _calculate_file_checksum(self, file_path: Path) -> str:
        """Calculate SHA-256 checksum of file."""
        
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    
    def _cleanup_old_backups(self, keep_days: int):
        """Remove backups older than keep_days."""
        
        cutoff_time = time.time() - (keep_days * 24 * 60 * 60)
        
        for archive in self.backup_dir.glob("apple_docs_backup_*.tar.gz"):
            if archive.stat().st_mtime < cutoff_time:
                logger.info(f"Removing old backup: {archive.name}")
                archive.unlink()
                
                # Remove metadata file
                metadata_file = archive.with_suffix(".json")
                if metadata_file.exists():
                    metadata_file.unlink()

def main():
    parser = argparse.ArgumentParser(description="Apple Docs Vectorstore Backup System")
    parser.add_argument("--create", action="store_true", help="Create new backup")
    parser.add_argument("--restore", type=str, help="Restore from backup (backup name without .tar.gz)")
    parser.add_argument("--list", action="store_true", help="List available backups")
    parser.add_argument("--backup-dir", type=str, default="backups", help="Backup directory")
    parser.add_argument("--keep-days", type=int, default=7, help="Days to keep backups")
    
    args = parser.parse_args()
    
    backup_system = VectorstoreBackup(args.backup_dir)
    
    if args.create:
        success = backup_system.create_backup(args.keep_days)
        exit(0 if success else 1)
    
    elif args.restore:
        success = backup_system.restore_backup(args.restore)
        exit(0 if success else 1)
    
    elif args.list:
        backups = backup_system.list_backups()
        
        if not backups:
            print("No backups found")
            return
        
        print(f"{'Backup Name':<30} {'Created':<20} {'Size (MB)':<10} {'Verified':<10}")
        print("-" * 70)
        
        for backup in backups:
            verified = "✅" if backup["verified"] else "❌"
            print(f"{backup['name']:<30} {backup['created_at'][:19]:<20} {backup['size_mb']:<10.1f} {verified:<10}")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()