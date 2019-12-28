from common import bean
import sys, os, re



def get_python_path():
    sys_path = os.environ['path'].split(';')
    pattern = "python[3]?(.exe)?$"

    for each in sys_path:
        for file in os.listdir(each):
            if re.match(pattern, file):
                return os.path.join(each, file)
    return None


if __name__ == '__main__':

    args = bean.Arg(sys.argv)
    py_path = args.get('python')

    if py_path is None:
        py_path = get_python_path()

    if py_path is None:
        raise Exception("未找到python环境")

    cmd = bean.CommandBuilder(py_path)

    cmd.add_arg(os.path.join(os.getcwd(), 'vtoc'))

    for arg in sys.argv[1:]:
        cmd.add_arg(arg)

    cmd.add_arg('--python=' + py_path)
    cmd.execute(False)
