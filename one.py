from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments


model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

training_args = TrainingArguments(
    output_dir="./results",          # output directory for model checkpoints
    num_train_epochs=3,              # number of training epochs
    per_device_train_batch_size=16,  # batch size per device during training
    per_device_eval_batch_size=64,   # batch size for evaluation
    warmup_steps=500,                # number of warmup steps for learning rate scheduler
    weight_decay=0.01,               # strength of weight decay
    logging_dir='./logs',            # directory for storing logs
)

_ = None

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=_,  # your training dataset
    eval_dataset=_,    # your evaluation dataset
)

trainer.train()
model.save_pretrained("./my_model")
