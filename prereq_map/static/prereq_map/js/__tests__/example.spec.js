import { mount } from '@vue/test-utils'
import Onbaording from '../components/onboarding.vue'

const { toMatchImageSnapshot } = require('jest-image-snapshot');

//import { toMatchImageSnapshot } from 'jest-image-snapshot'
expect.extend({ toMatchImageSnapshot });

const puppeteer = require('puppeteer');

describe('Example Component', () => {

    let browser;

    beforeAll(async () => {
        browser = await puppeteer.launch({
          args: ['--disable-dev-shm-usage']
        });
    });

    test('is a Vue instance', () => {
        const wrapper = mount(Onbaording)
        expect(wrapper.isVueInstance()).toBeTruthy()
    });

    test('renders correctly', () => {
        const wrapper = mount(Onbaording)
        expect(wrapper.element).toMatchSnapshot()
    });

    test('visual regression', async () => {

        const page = await browser.newPage();
        await page.goto('http://localhost:8123/course-search/');
        const screenshot = await page.screenshot();
        expect(screenshot).toMatchImageSnapshot();


    });

    afterAll(async () => {
        await browser.close();
    });

})
