import os


class BaseController():

    def view(self, path, args):
        package_path = os.environ.get('package', 'source')

        full_path = os.path.abspath(
            package_path +
            f'/core/resources/{self.resource_prefix}/{path}.html'
        )

        HTML_File = open(full_path, 'r')
        return HTML_File.read().format(data=args)
