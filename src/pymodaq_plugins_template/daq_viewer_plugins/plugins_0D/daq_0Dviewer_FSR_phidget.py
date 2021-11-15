import numpy as np
from easydict import EasyDict as edict
from pymodaq.daq_utils.daq_utils import ThreadCommand, getLineInfo, DataFromPlugins
from pymodaq.daq_viewer.utility_classes import DAQ_Viewer_base, comon_parameters, main
from pymodaq_plugins_template.hardware.FSR_phidget import FSR

class DAQ_0DViewer_FSR(DAQ_Viewer_base):
    """
    """
    params = comon_parameters+[
        ## TODO for your custom plugin
        # elements to be added here as dicts in order to control your custom stage
        ############
        ]

    def __init__(self, parent=None, params_state=None):
        super().__init__(parent, params_state)

    def commit_settings(self, param):
        """
        """
        pass

    def ini_detector(self, controller=None):
        """Detector communication initialization

        Parameters
        ----------
        controller: (object) custom object of a PyMoDAQ plugin (Slave case). None if only one detector by controller (Master case)

        Returns
        -------
        self.status (edict): with initialization status: three fields:
            * info (str)
            * controller (object) initialized controller
            *initialized: (bool): False if initialization failed otherwise True
        """

        try:
            self.status.update(edict(initialized=False,info="",x_axis=None,y_axis=None,controller=None))
            if self.settings.child(('controller_status')).value() == "Slave":
                if controller is None:
                    raise Exception('no controller has been defined externally while this detector is a slave one')
                else:
                    self.controller = controller
            else:
                self.controller = FSR()

            ## TODO for your custom plugin
            #initialize viewers pannel with the future type of data
            self.data_grabed_signal_temp.emit([DataFromPlugins(name='FSR',data=[np.array([0]), np.array([0])], dim='Data0D',
                                                          labels=['Mock1', 'label2'])])
            ##############################

            self.status.info = "Whatever info you want to log"
            self.status.initialized = True
            self.status.controller = self.controller
            return self.status

        except Exception as e:
            self.emit_status(ThreadCommand('Update_Status',[getLineInfo()+ str(e),'log']))
            self.status.info=getLineInfo()+ str(e)
            self.status.initialized=False
            return self.status

    def close(self):
        """
        Terminate the communication protocol
        """
        pass


    def grab_data(self, Naverage=1, **kwargs):
        """

        Parameters
        ----------
        Naverage: (int) Number of hardware averaging
        kwargs: (dict) of others optionals arguments
        """

        data_tot = self.controller.voltageRatioInput0.getVoltage()
        self.data_grabed_signal.emit([DataFromPlugins(name='FSR', data=data_tot,
                                                          dim='Data0D', labels=['dat0'])])

        # asynchrone version (non-blocking function with callback)
        raise NotImplemented  # when writing your own plugin remove this line
        self.controller.your_method_to_start_a_grab_snap(self.callback)  # when writing your own plugin replace this line
        #########################################################


    # def callback(self):
    #     """optional asynchrone method called when the detector has finished its acquisition of data"""
    #     data_tot = self.controller.your_method_to_get_data_from_buffer()
    #     self.data_grabed_signal.emit([DataFromPlugins(name='Mock1', data=data_tot,
    #                                               dim='Data0D', labels=['dat0', 'data1'])])
    #
    # def stop(self):
    #
    #     ## TODO for your custom plugin
    #     raise NotImplemented  # when writing your own plugin remove this line
    #     self.controller.your_method_to_stop_acquisition()  # when writing your own plugin replace this line
    #     self.emit_status(ThreadCommand('Update_Status', ['Some info you want to log']))
    #     ##############################
    #
    #     return ''


if __name__ == '__main__':
    main(__file__)
