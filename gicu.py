from seleniumbase import SB


with SB(uc=True, test=True) as mfsos:

    if True:
        url = "https://kick.com/brutalles"
        mfsos.uc_open_with_reconnect(url, 5)
        mfsos.uc_gui_click_captcha()
        mfsos.sleep(1)
        mfsos.uc_gui_handle_captcha()
        mfsos.sleep(1)
        if mfsos.is_element_present('button:contains("Accept")'):
            mfsos.uc_click('button:contains("Accept")', reconnect_time=4)
        if mfsos.is_element_visible('#injected-channel-player'):
            xvvxa = mfsos.get_new_driver(undetectable=True)
            xvvxa.uc_open_with_reconnect(url, 5)
            xvvxa.uc_gui_click_captcha()
            xvvxa.uc_gui_handle_captcha()
            mfsos.sleep(10)
            if xvvxa.is_element_present('button:contains("Accept")'):
                xvvxa.uc_click('button:contains("Accept")', reconnect_time=4)
            while mfsos.is_element_visible('#injected-channel-player'):
                mfsos.sleep(10)
            mfsos.quit_extra_driver()
    mfsos.sleep(1)

    mfsos.sleep(1)

