1、unittest原名为PyUnit，是由java的JUnit衍生而来。对于单元测试，需要设置预先条件，对比预期结果和实际结果；
2、unittest的流程：写好TestCase，然后由TestLoader加载TestCase到TestSuite，然后由TextTestRunner来运行TestSuite，运行的结果保存在TextTestResult中。我们通过命令行或者unittest.main()执行时，main会调用TextTestRunner中的run来执行，或者我们可以直接通过TextTestRunner来执行用例；
3、参数verbosity可以控制执行结果的输出，0 是简单报告、1 是一般报告（默认值）、2 是详细报告。