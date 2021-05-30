#!/usr/bin/python3

import threading
from flask import Response
from flask import Flask
from flask import jsonify
from flask import render_template
from terrariumController.terrarium_controller import TerrariumController
from lib.delivery.decorator import stats_decorator

import argparse

stream = WebStream()
app = Flask(__name__)

terrarium_controller = TerrariumController()
terrarium_controller.start_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/thermostate/target_temp/<int:section>/<int:temp>")
def set_target_temp(section=None, temp=None):
    terrarium_controller.set_target_temp(section, temp)

    return jsonify({'status': 'No action performed'})


@app.route("/thermostate/toggle/<int:section>/<int:value>")
def toggle_thermostate(section=None, value=None):
    terrarium_controller.toggle_thermostat(section, value)

    return jsonify({'status': 'No action performed'})


@app.route("/thermostate/temp_offset/<int:section>/<int:offset>")
def set_temp_offset(section=None, offset=None):
    terrarium_controller.set_temp_offset(section, offset)

    return jsonify({'status': 'No action performed'})


@app.route("/thermostate/status/<int:section>")
def status(section=None):
    status = stats_decorator.decorate(
        terrarium_controller.read_status(section)
    )

    return jsonify(status=status)


# def create_thread():
#     thread = threading.Thread(target=stream.detect_motion, args=(
#         args["frame_count"],))
#
#     thread.daemon = True
#     return thread


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--ip", type=str, required=True,
                    help="ip address of the device")
    ap.add_argument("-o", "--port", type=int, required=True,
                    help="ephemeral port number of the server (1024 to 65535)")
    ap.add_argument("-f", "--frame-count", type=int, default=32,
                    help="# of frames used to construct the background model")
    args = vars(ap.parse_args())

    app.run(host=args["ip"], port=args["port"], debug=True,
            threaded=True, use_reloader=False)

# stream.stop()
