import profile
import pstats


def runtime_analysis(func):
    profiler = profile.Profile()
    profiler.runcall(func)
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()
