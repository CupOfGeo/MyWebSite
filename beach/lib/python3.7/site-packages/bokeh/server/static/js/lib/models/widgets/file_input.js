import { Widget, WidgetView } from "./widget";
export class FileInputView extends WidgetView {
    connect_signals() {
        super.connect_signals();
        this.connect(this.model.change, () => this.render());
        this.connect(this.model.properties.width.change, () => this.render());
    }
    render() {
        if (this.dialogEl == null) {
            this.dialogEl = document.createElement('input');
            this.dialogEl.type = "file";
            this.dialogEl.multiple = this.model.multiple;
            this.dialogEl.onchange = () => {
                const { files } = this.dialogEl;
                if (files != null) {
                    this.load_files(files);
                }
            };
            this.el.appendChild(this.dialogEl);
        }
        if (this.model.accept != null && this.model.accept != '')
            this.dialogEl.accept = this.model.accept;
        this.dialogEl.style.width = `{this.model.width}px`;
        this.dialogEl.disabled = this.model.disabled;
    }
    async load_files(files) {
        const value = [];
        const filename = [];
        const mime_type = [];
        let i;
        for (i = 0; i < files.length; i++) {
            filename.push(files[i].name);
            const data_url = await this.readfile(files[i]);
            const [, mime, , data] = data_url.split(/[:;,]/, 4);
            value.push(data);
            mime_type.push(mime);
        }
        if (this.model.multiple) {
            this.model.filename = filename;
            this.model.mime_type = mime_type;
            this.model.value = value;
        }
        else {
            this.model.filename = filename[0];
            this.model.mime_type = mime_type[0];
            this.model.value = value[0];
        }
    }
    readfile(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = () => {
                const { result } = reader;
                if (result != null) {
                    resolve(result);
                }
                else {
                    reject(reader.error ?? new Error(`unable to read '${file.name}'`));
                }
            };
            reader.readAsDataURL(file);
        });
    }
}
FileInputView.__name__ = "FileInputView";
export class FileInput extends Widget {
    constructor(attrs) {
        super(attrs);
    }
    static init_FileInput() {
        this.prototype.default_view = FileInputView;
        this.define(({ Boolean, String, Array, Or }) => ({
            value: [Or(String, Array(String)), ""],
            mime_type: [Or(String, Array(String)), ""],
            filename: [Or(String, Array(String)), ""],
            accept: [String, ""],
            multiple: [Boolean, false],
        }));
    }
}
FileInput.__name__ = "FileInput";
FileInput.init_FileInput();
//# sourceMappingURL=file_input.js.map