import os

dirs = [
    os.path.join('Data','raw'),
    os.path.join('Data','processed'),
    'notebooks',
    'saved_models',
    os.path.join('src','pipeline')
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    
files = [
    os.path.join('src','pipeline','train_pipeline.py'),
    '.gitignore',
    'setup.py',
    'requirements.txt',
    'README.md',
    os.path.join('src','__init__.py'),
    os.path.join('src','data_ingestion.py'),
    os.path.join('src','data_transformation.py'),
    os.path.join('src','model_training.py'),
    os.path.join('src','model_deployment.py'),
    os.path.join('src','pipeline','deploy_pipeline.py'),
]

for file_ in files:
    with open (file_,'w') as f:
        pass