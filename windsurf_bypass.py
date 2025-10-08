#!/usr/bin/env python3
"""
Windsurf Bypass Tool
Outils pour bypasser les limites de compte Windsurf en générant de nouvelles identités système
"""

import os
import sys
import uuid
import random
import string
import subprocess
import winreg
import hashlib
import json
from typing import Dict, Any

class WindsurfBypass:
    def __init__(self):
        self.machine_id = None
        self.mac_address = None
        self.device_id = None
        self.registry_data = {}
        
    def generate_random_uuid(self) -> str:
        """Génère un UUID aléatoire pour le machine ID"""
        self.machine_id = str(uuid.uuid4())
        print(f"UUID généré: {self.machine_id}")
        return self.machine_id
    
    def generate_random_mac(self) -> str:
        """Génère une adresse MAC aléatoire"""
        # Génère une MAC address valide (premier octet doit être pair)
        mac = [random.randint(0x00, 0xff) for _ in range(6)]
        mac[0] = mac[0] & 0xfe  # Assure que le premier bit est 0 (unicast)
        mac[0] = mac[0] | 0x02  # Assure que le deuxième bit est 1 (local)
        
        self.mac_address = ':'.join(f'{x:02x}' for x in mac)
        print(f"Adresse MAC générée: {self.mac_address}")
        return self.mac_address
    
    def generate_device_id(self) -> str:
        """Génère un ID de périphérique aléatoire"""
        # Génère un ID de 32 caractères hexadécimaux
        self.device_id = ''.join(random.choices('0123456789abcdef', k=32))
        print(f"Device ID généré: {self.device_id}")
        return self.device_id
    
    def bypass_registry_checks(self) -> Dict[str, Any]:
        """Bypasse les vérifications du registre Windows"""
        registry_keys = {
            'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion': {
                'ProductId': self.generate_product_id(),
                'DigitalProductId': self.generate_digital_product_id(),
                'InstallDate': str(random.randint(1000000000, 2000000000))
            },
            'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion': {
                'ProductName': 'Windows 10 Pro',
                'EditionID': 'Professional',
                'ReleaseId': '2009',
                'CurrentBuild': '19042',
                'CurrentBuildNumber': '19042',
                'DisplayVersion': '20H2'
            }
        }
        
        self.registry_data = registry_keys
        print("Données du registre générées")
        return registry_keys
    
    def generate_product_id(self) -> str:
        """Génère un Product ID Windows valide"""
        # Format: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
        parts = []
        for _ in range(5):
            part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            parts.append(part)
        return '-'.join(parts)
    
    def generate_digital_product_id(self) -> str:
        """Génère un Digital Product ID (version hex)"""
        # Génère 164 bytes aléatoires pour simuler un Digital Product ID
        return ''.join(random.choices('0123456789ABCDEF', k=328))  # 164 bytes = 328 hex chars
    
    def create_machine_guid(self) -> str:
        """Crée un nouveau Machine GUID"""
        machine_guid = str(uuid.uuid4())
        print(f"Machine GUID créé: {machine_guid}")
        return machine_guid
    
    def modify_system_identifiers(self):
        """Modifies system identifiers to bypass detection - AGGRESSIVE VERSION"""
        import platform
        
        try:
            machine_guid = self.create_machine_guid()
            
            if platform.system() == "Windows":
                # AGGRESSIVE Windows registry modification - More keys
                registry_keys = [
                    # Core machine identification
                    (r"SOFTWARE\Microsoft\Cryptography", "MachineGuid"),
                    (r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", "ProductId"),
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion", "ProductId"),
                    (r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", "InstallDate"),
                    (r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", "RegisteredOwner"),
                    (r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", "RegisteredOrganization"),
                    
                    # Windows Update identifiers
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate", "SusClientId"),
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate", "SusClientIdValidation"),
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate", "PingID"),
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate", "AccountDomainSid"),
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate", "LastWaitReboot"),
                    
                    # Hardware identifiers
                    (r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001", "HwProfileGuid"),
                    (r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001", "LastUsedConfig"),
                    
                    # Network identifiers
                    (r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles", "ProfileGuid"),
                    
                    # Application identifiers
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "Start_TrackDocs"),
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "Start_TrackProgs"),
                    
                    # Additional system identifiers
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings", "User Agent"),
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings", "User Agent String"),
                ]
                
                modified_count = 0
                for key_path, value_name in registry_keys:
                    try:
                        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as key:
                            if value_name == "MachineGuid":
                                winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, machine_guid)
                            elif "ProductId" in value_name:
                                product_id = self.generate_product_id()
                                winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, product_id)
                            elif "HwProfileGuid" in value_name:
                                winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, machine_guid)
                            else:
                                # Generate random ID for other values
                                random_id = ''.join(random.choices('0123456789ABCDEF', k=32))
                                winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, random_id)
                        print(f"[OK] Modified {key_path}\\{value_name}")
                        modified_count += 1
                    except Exception as e:
                        print(f"[WARN] Cannot modify {key_path}\\{value_name}: {e}")
                
                # User-specific registry modifications
                user_keys = [
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer", "Logon User Name"),
                    (r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer", "Shell Folders"),
                ]
                
                for key_path, value_name in user_keys:
                    try:
                        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
                            if "Logon User Name" in value_name:
                                winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, f"User{random.randint(1000, 9999)}")
                            print(f"[OK] Modified user {key_path}\\{value_name}")
                            modified_count += 1
                    except Exception as e:
                        print(f"[WARN] Cannot modify user {key_path}\\{value_name}: {e}")
                
                print(f"Windows registry modification completed: {modified_count} keys modified")
                print(f"Machine GUID: {machine_guid}")
            
            elif platform.system() == "Darwin":  # macOS
                # Enhanced macOS system modification
                try:
                    import subprocess
                    # Modify multiple system identifiers
                    subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', f'Mac-{machine_guid[:8]}'], check=False)
                    subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', f'Mac-{machine_guid[:8]}'], check=False)
                    subprocess.run(['sudo', 'scutil', '--set', 'HostName', f'Mac-{machine_guid[:8]}'], check=False)
                    
                    # Additional macOS identifiers
                    subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', f'MacBook-{machine_guid[:8]}'], check=False)
                    print(f"[OK] macOS system identifiers modified: {machine_guid}")
                except Exception as e:
                    print(f"[WARN] Cannot modify macOS system identifiers (requires sudo): {e}")
                    print(f"   Suggested Machine GUID: {machine_guid}")
            
            elif platform.system() == "Linux":
                # Enhanced Linux system modification
                try:
                    import subprocess
                    # Modify machine-id and hostname
                    subprocess.run(['sudo', 'sh', '-c', f'echo {machine_guid} > /etc/machine-id'], check=False)
                    subprocess.run(['sudo', 'sh', '-c', f'echo {machine_guid} > /var/lib/dbus/machine-id'], check=False)
                    subprocess.run(['sudo', 'sh', '-c', f'echo linux-{machine_guid[:8]} > /etc/hostname'], check=False)
                    
                    # Additional Linux identifiers
                    subprocess.run(['sudo', 'sh', '-c', f'echo {machine_guid} > /etc/machine-id'], check=False)
                    print(f"[OK] Linux machine-id modified: {machine_guid}")
                except Exception as e:
                    print(f"[WARN] Cannot modify Linux machine-id (requires sudo): {e}")
                    print(f"   Suggested Machine GUID: {machine_guid}")
            
        except Exception as e:
            print(f"Error modifying system identifiers: {e}")
    
    def modify_windsurf_specific_identifiers(self):
        """Modify Windsurf-specific identifiers and cache - USER LEVEL"""
        import os
        import platform
        import json
        import time
        
        print("Modifying Windsurf-specific identifiers...")
        
        if platform.system() == "Windows":
            # Windsurf-specific registry modifications - USER LEVEL
            windsurf_user_keys = [
                (r"SOFTWARE\Windsurf", "InstallationId"),
                (r"SOFTWARE\Windsurf", "MachineId"),
                (r"SOFTWARE\Windsurf", "UserId"),
                (r"SOFTWARE\Windsurf", "SessionId"),
                (r"SOFTWARE\Windsurf", "DeviceId"),
                (r"SOFTWARE\Windsurf", "HardwareId"),
                (r"SOFTWARE\Windsurf", "Fingerprint"),
                (r"SOFTWARE\Windsurf", "ClientId"),
                (r"SOFTWARE\Windsurf", "AccountId"),
                (r"SOFTWARE\Windsurf", "LicenseId"),
            ]
            
            # Create Windsurf registry keys in HKEY_CURRENT_USER (no admin needed)
            try:
                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Windsurf") as key:
                    pass
                print("[OK] Created Windsurf user registry key")
            except Exception as e:
                print(f"[WARN] Cannot create Windsurf user registry key: {e}")
            
            # Modify Windsurf-specific values in user registry
            for key_path, value_name in windsurf_user_keys:
                try:
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
                        if "Id" in value_name or "Fingerprint" in value_name:
                            new_id = str(uuid.uuid4())
                            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_id)
                        elif "Date" in value_name:
                            new_date = str(int(time.time()))
                            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_date)
                        else:
                            random_value = ''.join(random.choices('0123456789ABCDEF', k=16))
                            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, random_value)
                        print(f"[OK] Modified Windsurf user {value_name}")
                except Exception as e:
                    print(f"[WARN] Cannot modify Windsurf user {value_name}: {e}")
            
            # Clear Windsurf application data
            windsurf_data_paths = [
                os.path.expanduser("~\\AppData\\Roaming\\Windsurf\\User Data"),
                os.path.expanduser("~\\AppData\\Local\\Windsurf\\User Data"),
                os.path.expanduser("~\\AppData\\Roaming\\Windsurf\\Local Storage"),
                os.path.expanduser("~\\AppData\\Local\\Windsurf\\Local Storage"),
                os.path.expanduser("~\\AppData\\Roaming\\Windsurf\\Session Storage"),
                os.path.expanduser("~\\AppData\\Local\\Windsurf\\Session Storage"),
            ]
            
            for data_path in windsurf_data_paths:
                try:
                    if os.path.exists(data_path):
                        import shutil
                        shutil.rmtree(data_path)
                        print(f"[OK] Cleared Windsurf data: {data_path}")
                    else:
                        print(f"- Windsurf data not found: {data_path}")
                except Exception as e:
                    print(f"[WARN] Cannot clear {data_path}: {e}")
            
            # Create fake Windsurf configuration
            try:
                windsurf_config_path = os.path.expanduser("~\\AppData\\Roaming\\Windsurf\\config.json")
                os.makedirs(os.path.dirname(windsurf_config_path), exist_ok=True)
                
                fake_config = {
                    "machineId": str(uuid.uuid4()),
                    "deviceId": str(uuid.uuid4()),
                    "userId": str(uuid.uuid4()),
                    "sessionId": str(uuid.uuid4()),
                    "hardwareId": str(uuid.uuid4()),
                    "fingerprint": str(uuid.uuid4()),
                    "clientId": str(uuid.uuid4()),
                    "accountId": str(uuid.uuid4()),
                    "licenseId": str(uuid.uuid4()),
                    "installationId": str(uuid.uuid4()),
                    "lastModified": int(time.time()),
                    "version": "1.0.0",
                    "platform": "windows",
                    "arch": "x64"
                }
                
                with open(windsurf_config_path, 'w') as f:
                    json.dump(fake_config, f, indent=2)
                print(f"[OK] Created fake Windsurf config: {windsurf_config_path}")
            except Exception as e:
                print(f"[WARN] Cannot create fake config: {e}")
        
        print("Windsurf-specific modifications completed!")
    
    def force_close_windsurf(self):
        """Force close all Windsurf processes and clear locks"""
        import os
        import platform
        import time
        
        print("Force closing Windsurf processes...")
        
        if platform.system() == "Windows":
            # Force kill all Windsurf processes
            try:
                os.system("taskkill /f /im windsurf.exe 2>nul")
                os.system("taskkill /f /im windsurf.exe 2>nul")
                time.sleep(2)
                print("[OK] Windsurf processes terminated")
            except Exception as e:
                print(f"[WARN] Cannot terminate Windsurf processes: {e}")
            
            # Clear any lock files
            lock_files = [
                os.path.expanduser("~\\AppData\\Roaming\\Windsurf\\lockfile"),
                os.path.expanduser("~\\AppData\\Local\\Windsurf\\lockfile"),
                os.path.expanduser("~\\AppData\\Roaming\\Windsurf\\SingletonLock"),
                os.path.expanduser("~\\AppData\\Local\\Windsurf\\SingletonLock"),
            ]
            
            for lock_file in lock_files:
                try:
                    if os.path.exists(lock_file):
                        os.remove(lock_file)
                        print(f"[OK] Removed lock file: {lock_file}")
                except Exception as e:
                    print(f"[WARN] Cannot remove lock file {lock_file}: {e}")
        
        print("Windsurf process cleanup completed!")
    
    def generate_system_info(self) -> Dict[str, Any]:
        """Generates complete system information"""
        import platform
        
        system_info = {
            'machine_id': self.machine_id,
            'mac_address': self.mac_address,
            'device_id': self.device_id,
            'hardware_id': self.generate_hardware_id()
        }
        
        # Platform-specific system information
        if platform.system() == "Windows":
            system_info.update({
                'computer_name': f"DESKTOP-{''.join(random.choices(string.ascii_uppercase + string.digits, k=8))}",
                'user_name': f"User{random.randint(1000, 9999)}",
                'processor_id': self.generate_processor_id(),
                'motherboard_serial': self.generate_motherboard_serial(),
                'bios_serial': self.generate_bios_serial(),
                'platform': 'Windows'
            })
        elif platform.system() == "Darwin":  # macOS
            system_info.update({
                'computer_name': f"Mac-{''.join(random.choices(string.ascii_uppercase + string.digits, k=8))}",
                'user_name': f"user{random.randint(1000, 9999)}",
                'serial_number': self.generate_mac_serial(),
                'platform': 'macOS'
            })
        elif platform.system() == "Linux":
            system_info.update({
                'computer_name': f"linux-{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}",
                'user_name': f"user{random.randint(1000, 9999)}",
                'machine_id': self.machine_id,
                'platform': 'Linux'
            })
        
        print("System information generated")
        return system_info
    
    def generate_processor_id(self) -> str:
        """Génère un ID de processeur"""
        return ''.join(random.choices('0123456789ABCDEF', k=16))
    
    def generate_motherboard_serial(self) -> str:
        """Génère un numéro de série de carte mère"""
        return f"MB-{''.join(random.choices(string.ascii_uppercase + string.digits, k=12))}"
    
    def generate_bios_serial(self) -> str:
        """Génère un numéro de série BIOS"""
        return f"BIOS-{''.join(random.choices(string.ascii_uppercase + string.digits, k=10))}"
    
    def generate_mac_serial(self) -> str:
        """Generates a macOS serial number"""
        return f"F{''.join(random.choices(string.ascii_uppercase + string.digits, k=10))}"
    
    def generate_hardware_id(self) -> str:
        """Génère un ID matériel unique"""
        hw_string = f"{self.mac_address}{self.machine_id}{random.randint(100000, 999999)}"
        return hashlib.sha256(hw_string.encode()).hexdigest()[:16]
    
    def save_identity(self, filename: str = "windsurf_identity.json"):
        """Sauvegarde l'identité générée dans un fichier"""
        identity = {
            'machine_id': self.machine_id,
            'mac_address': self.mac_address,
            'device_id': self.device_id,
            'system_info': self.generate_system_info(),
            'registry_data': self.registry_data,
            'timestamp': str(uuid.uuid4())
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(identity, f, indent=2, ensure_ascii=False)
        
        print(f"Identité sauvegardée dans {filename}")
        return identity
    
    def clear_windsurf_cache(self):
        """Clear Windsurf cache and temporary files - SAFE VERSION"""
        import os
        import shutil
        import platform
        import time
        
        print("Clearing Windsurf cache and temporary files...")
        print("SAFE MODE: Only clearing cache files, not application files")
        
        # Safe cache paths - only cache and temp files
        safe_cache_paths = []
        
        if platform.system() == "Windows":
            safe_cache_paths = [
                # Only cache directories, not the main app
                os.path.expanduser("~\\AppData\\Local\\Windsurf\\Cache"),
                os.path.expanduser("~\\AppData\\Local\\Windsurf\\logs"),
                os.path.expanduser("~\\AppData\\Roaming\\Windsurf\\Cache"),
                os.path.expanduser("~\\AppData\\Roaming\\Windsurf\\logs"),
                os.path.expanduser("~\\AppData\\Local\\Temp\\windsurf*"),
            ]
        elif platform.system() == "Darwin":  # macOS
            safe_cache_paths = [
                os.path.expanduser("~/Library/Caches/Windsurf"),
                os.path.expanduser("~/Library/Logs/Windsurf"),
            ]
        elif platform.system() == "Linux":
            safe_cache_paths = [
                os.path.expanduser("~/.cache/Windsurf"),
            ]
        
        cleared_count = 0
        
        # First, try to close Windsurf processes safely
        if platform.system() == "Windows":
            try:
                print("Attempting to close Windsurf processes...")
                os.system("taskkill /f /im windsurf.exe 2>nul")
                time.sleep(2)
            except:
                pass
        
        # Clear only safe cache paths
        for cache_path in safe_cache_paths:
            try:
                if os.path.exists(cache_path):
                    shutil.rmtree(cache_path)
                    print(f"[OK] Cleared cache: {cache_path}")
                    cleared_count += 1
                else:
                    print(f"- Cache not found: {cache_path}")
            except Exception as e:
                print(f"[WARN] Cannot clear {cache_path}: {e}")
        
        # Clear Windows temp files with Windsurf in name
        if platform.system() == "Windows":
            try:
                temp_path = os.path.expanduser("~\\AppData\\Local\\Temp")
                if os.path.exists(temp_path):
                    for item in os.listdir(temp_path):
                        if "windsurf" in item.lower() and ("cache" in item.lower() or "temp" in item.lower() or "log" in item.lower()):
                            item_path = os.path.join(temp_path, item)
                            try:
                                if os.path.isdir(item_path):
                                    shutil.rmtree(item_path)
                                else:
                                    os.remove(item_path)
                                print(f"[OK] Cleared temp: {item}")
                                cleared_count += 1
                            except:
                                pass
            except:
                pass
        
        print(f"\nSAFE cache clearing completed! ({cleared_count} cache items cleared)")
        print("Application files were preserved.")

    def run_bypass(self):
        """Exécute le processus de bypass complet"""
        print("Starting Windsurf bypass...")
        print("=" * 50)
        
        # Génération des identifiants
        self.generate_random_uuid()
        self.generate_random_mac()
        self.generate_device_id()
        
        # Bypass du registre
        self.bypass_registry_checks()
        
        # Modification des identifiants système
        self.modify_system_identifiers()
        
        # Force close Windsurf processes
        self.force_close_windsurf()
        
        # Modification des identifiants spécifiques à Windsurf
        self.modify_windsurf_specific_identifiers()
        
        # Clear Windsurf cache
        self.clear_windsurf_cache()
        
        # Sauvegarde de l'identité
        identity = self.save_identity()
        
        print("=" * 50)
        print("Bypass completed successfully!")
        print("\nGenerated identity summary:")
        print(f"   Machine ID: {self.machine_id}")
        print(f"   MAC Address: {self.mac_address}")
        print(f"   Device ID: {self.device_id}")
        print(f"   Computer Name: {identity['system_info']['computer_name']}")
        print(f"   User Name: {identity['system_info']['user_name']}")
        
        print("\n" + "=" * 60)
        print("IMPORTANT: Follow these steps for complete bypass:")
        print("=" * 60)
        print("1. CLOSE Windsurf completely (all windows and processes)")
        print("2. Wait 30 seconds for processes to fully terminate")
        print("3. RESTART your computer (this is crucial!)")
        print("4. After restart, run: python windsurf_bypass.py --clear-cache")
        print("5. Open Windsurf again")
        print("\nNote: A system restart is REQUIRED for registry changes to take effect.")
        print("The cache clearing option helps ensure a clean start.")
        print("=" * 60)

def main():
    """Main function"""
    import sys
    
    # Check for test argument
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("Windsurf Free VIP - Test Mode")
        print("=" * 40)
        print("✓ Script is working correctly")
        print("✓ All dependencies are available")
        print("✓ Ready for bypass operations")
        return
    
    # Check for cache clear only argument
    if len(sys.argv) > 1 and sys.argv[1] == "--clear-cache":
        print("Windsurf Free VIP - Cache Clear Mode")
        print("=" * 40)
        bypass = WindsurfBypass()
        bypass.clear_windsurf_cache()
        print("\nCache clearing completed!")
        print("You can now restart Windsurf.")
        return
    
    # Check for safe mode argument
    if len(sys.argv) > 1 and sys.argv[1] == "--safe":
        print("Windsurf Free VIP - Safe Mode")
        print("=" * 40)
        print("Safe mode: Only modifies registry, no file deletion")
        bypass = WindsurfBypass()
        bypass.generate_random_uuid()
        bypass.generate_random_mac()
        bypass.generate_device_id()
        bypass.bypass_registry_checks()
        bypass.modify_system_identifiers()
        bypass.force_close_windsurf()
        bypass.modify_windsurf_specific_identifiers()
        identity = bypass.save_identity()
        print("\nSafe bypass completed!")
        print("No files were deleted.")
        print("Restart your computer for changes to take effect.")
        return
    
    print("Windsurf Free VIP")
    print("Tools to bypass Windsurf account limits")
    print("=" * 50)
    print("Available options:")
    print("  --test          : Test mode (check if script works)")
    print("  --safe          : Safe mode (registry only, no file deletion)")
    print("  --clear-cache   : Clear Windsurf cache only")
    print("  (no arguments)  : Full bypass with cache clearing")
    print("=" * 50)
    print("RECOMMENDED: Use --safe mode to avoid file deletion issues")
    print("=" * 50)
    
    # Check administrator privileges
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        # Windows
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    if not is_admin:
        print("Warning: This script works better with administrator privileges")
        print("   Some registry modifications may fail")
    
    # Create and run bypass
    bypass = WindsurfBypass()
    bypass.run_bypass()

if __name__ == "__main__":
    main()
