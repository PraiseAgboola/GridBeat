{  
  "{pkgs ? import <nixpkgs> {}}": {  
    "packages": [  
      "playwright",  
      "python3",  
      "nodejs"  
    ],  
    "shellHook": ''"  
      # Activate Playwright dependencies  
      export PLAYWRIGHT_BROWSERS_PATH=0  
      # Add your custom environment setup here  
    ''  
  }  
}