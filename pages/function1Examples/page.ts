import type { ComponentPageScheme } from "jit";
import { Jit } from "jit";
import schemeJson from "./scheme.json";
type BaseComponent = InstanceType<typeof Jit.BaseComponent>;

class PageCls extends Jit.GridPage {
    Form3!: BaseComponent;
    Modal2!: BaseComponent;
    Table1!: BaseComponent;
    scheme: ComponentPageScheme = schemeJson;

    bindEvent() {
        this.subscribeEvent("AI:aiagent_lbNEkO.beforeNodeRun", async (
            {
                data
            }
        ) => {
            this.app.modules.FeedBack.globalMessage("info", "Starting the process...");
        });

        this.Table1.subscribeEvent("clicknGdlrp", async () => {
            this.Modal2.call("edit");
            this.Form3.mode.value = "edit";
            this.Form3.formData.value = this.Table1.activeRow.value;
        });

        this.Table1.subscribeEvent("clickjWngef", async () => {
            const globalConfirmResult1 = Jit.datatypes.Dropdown(await this.app.modules.FeedBack.globalConfirm("Confirm deletion"), {
                "name": "confirmationOfResults",
                "title": "result",

                "options": [{
                    "value": "true",
                    "label": "Confirm"
                }, {
                    "value": "false",
                    "label": "Cancel"
                }],

                "color": true,
                "placeholder": "",
                "selectionWay": "custom",
                "allowManualInput": false,

                "mulLevelSelectionConfig": {
                    "sortFieldName": "",
                    "sortBy": "",
                    "matchFieldName": "",
                    "dataSourceModel": "",
                    "filterValue": ""
                }
            });

            if (globalConfirmResult1.isEqual("true")) {
                await this.Table1.activeRow.delete(undefined);
                await this.Table1.refresh();
            }
        });

        this.Table1.subscribeEvent("clicksymfQq", async () => {
            this.Modal2.call("Data Entry");
            this.Form3.mode.value = "add";
            this.Form3.formData.reset();
        });

        this.Form3.subscribeEvent("afterSubmit", async () => {
            this.Modal2.close();
            await this.Table1.refresh();
        });

        this.subscribeEvent("AI:aiagent_lbNEkO.afterNodeRun", async (
            {
                data
            }
        ) => {
            this.app.modules.FeedBack.globalMessage("info", "Processing complete!");
            await this.Table1.call(undefined);
        });
    }
}

export default PageCls;