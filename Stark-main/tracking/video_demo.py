import os
import sys
import argparse

prj_path = os.path.join(os.path.dirname(__file__), '..')
if prj_path not in sys.path:
    sys.path.append(prj_path)

from lib.test.evaluation import Tracker


def run_video(tracker_name, tracker_param, videofile, optional_box=None, debug=None, save_results=False):
    """Run the tracker on your webcam.
    args:
        tracker_name: Name of tracking method.
        tracker_param: Name of parameter file.
        debug: Debug level.
    """
    tracker = Tracker(tracker_name, tracker_param, "video")
    tracker.run_video(videofilepath=videofile, optional_box=optional_box, debug=debug, save_results=save_results)


def main():
    tracker_name = 'stark_st'
    tracker_param = 'baseline_R101'
    videofile = '../../ppap.mp4'
    optional_box = None #optional_box with format x y w h.
    debug= 0
    save_results= True #Save bounding boxes

    run_video(tracker_name, tracker_param, videofile, optional_box, debug, save_results)


if __name__ == '__main__':
    main()
