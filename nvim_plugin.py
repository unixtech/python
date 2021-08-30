import pynvim


@pynvim.plugin
class TestPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim


    @pynvim.function('TestFunction')
    def testFunction(self, args):
        self.nvim.current.line = 'Hello from your plugin'