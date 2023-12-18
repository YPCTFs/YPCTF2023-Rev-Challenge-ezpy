# gen pyc
import py_compile
import pathlib
import shutil

def gen_pyc(path):
    if not pathlib.Path(path).exists():
        raise Exception('path not exists')

    # if cache exists, rm it
    if pathlib.Path(path).joinpath('__pycache__').exists():
           shutil.rmtree(pathlib.Path(path).joinpath('__pycache__'))

    for p in pathlib.Path(path).glob('**/*.py'):
        py_compile.compile(p)

    # crete target dir
    pathlib.Path(path).parent.joinpath('target').mkdir(exist_ok=True)
    # move pyc to target
    for p in pathlib.Path(path).glob('**/*.pyc'):
        shutil.move(p, pathlib.Path(path).parent.joinpath('target').joinpath(p.name))
    # rm cache
    for p in pathlib.Path(path).glob('**/__pycache__'):
        p.rmdir()
    print('gen pyc done')


if __name__ == '__main__':
    gen_pyc('./src')
